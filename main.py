import sys
from Pub import Pub 
from Sub import Sub
import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import Ui_MainWindow
import threading
from PIL import Image
from PIL.ImageQt import ImageQt
import os
from PyQt5.QtCore import QThread, pyqtSignal
from config import server, RPI_ID, global_topic, pub_topic, sub_topic, path, ROOT
from helpers import get_now_string
from Database import Database


class GUI(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.path = path
        # set exposure time slider
        self.slider_expTime.setMaximum(10000000)
        self.slider_expTime.setMinimum(1)
        self.slider_expTime.setSliderPosition(6)
        
        # set ISO slider
        self.slider_iso.setMaximum(800)
        self.slider_iso.setMinimum(100)
        self.slider_iso.setSliderPosition(400)
        
        # set Brightness Slider
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setSliderPosition(50)
        
        # set Contrast Slider
        self.slider_contrast.setMaximum(100)
        self.slider_contrast.setMinimum(-100)
        self.slider_contrast.setSliderPosition(0)
        
        # set Saturation Slider
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setMinimum(-100)
        self.slider_saturation.setSliderPosition(0)
        
        # set Sharpness Slider
        self.slider_sharpness.setMaximum(100)
        self.slider_sharpness.setMinimum(-100)
        self.slider_sharpness.setSliderPosition(0)
        
        # camera settings its fix according to doc of PiCamera
        #https://picamera.readthedocs.io/en/release-1.2/api.html
        exp_mode = ['off', 'auto','night','nightpreview',
                              'backlight','spotlight','sports','snow',
                              'beach','verylong','fixedfps','antishake','fireworks'
                              ]
        wb = ['off', 'auto', 'sunlight','cloudy', 'shade', 'tungsten',
                              'fluorescent', 'incandescent', 'flash','horizon'
                              ]
        raw = ['jpeg','png','rgb','yuv'
                ]
        # params for camera sensor set form GUI
        self.params = {
            'imageName':'test.png',
            'time':'123',
            'resolution':(100, 100), # width , height
            'expose_time': 6 ,# from 1-10 seconds (v1 support 6sec and v2 support 10 seconds),
            'exposure_mode': 'auto',
            'white_balance': 'auto',
            'iso': 400, # 100 to 800 
            'brightness': 50, # 0 to 100 , default = 50
            'contrast': 0, # -100 to 100 , default = 50
            'saturation': 0, # -100 to 100 , default = 0
            'sharpness': 0, # -100 to 100 , default = 0
            'raw': 'png',
            }
        for x in exp_mode:
            self.cb_expMode.addItem(x)
        
        for x in wb:
            self.cb_whiteBalanceMode.addItem(x)
            
        for x in raw :
            self.cb_raw.addItem(x)
            
        
        
        pass # end on __init__ function of GUI
    
    def load_image(self):
        selected_image = self.cb_select_image.currentText()
        if len(selected_image) > 0:
            input_image = Image.open(f'{self.path}{selected_image}')#imread(image_name)
            im = input_image.convert("RGBA")
            data = im.tobytes("raw", "RGBA")
            
            qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)

            pixmap = QPixmap.fromImage(qim)
            self.pixmap = QPixmap(pixmap)
            self.lbl_Image.setPixmap(self.pixmap)
            self.lbl_Image.setAlignment(QtCore.Qt.AlignCenter)
            self.lbl_Image.setScaledContents(True)
            self.lbl_Image.setMinimumSize(1,1)
            self.lbl_Image.show()
        else:
            print('NOTE: No Image found in Drop Down Selection')
        pass # end of load image function
        
        
    pass


class MAIN(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.thread_loop = True
        
        # display GUI 
        self.gui = GUI()
        self.gui.show()
        
        # database Init
        self.db = Database()
        
        # other static varibles
        port = 1883
        self.ROOT = ROOT
        self.path = path
        self.ImageName = ''
        self.Iwidth = 100
        self.Iheight = 100
        
        # init rpi as publisher with unique id (used in MQTT topic)
        self.pub = Pub(RPI_ID, server, port)
        self.pub.signal_loadImages.connect(self.gui.load_image)
        # init rpi as subscriber to subscripbe all rpi's in define MQTT topic
        self.sub = Sub(server, port, self.path, RPI_ID)
        # sub class signal emiters
        self.sub.signal_sub.connect(self.send_feedback_to_publisher)
        self.sub.signal_log.connect(self.update_log)
        
        # set booleans for GUI Int
        self.shoot = False
        self.load_images = False
        self.ul = False
        self.ul_mesg = ""
        
        # fill the cb if there is any image in Image Folder
        self.update_cb_images("Update Images")
        
        try:
            self.gui.load_image(self.path)
        except:
            pass
        #clickable(self.txtPassword).connect(self.presstxt_password)
        self.gui.btn_shoot.clicked.connect(lambda: self.press_shoot())
        self.gui.btn_loadImage.clicked.connect(lambda: self.gui.load_image())
        self.gui.btn_exit.clicked.connect(lambda: self.closeApp())
        
        self.load_data_to_gui()
        pass # end of main __init__ function
    
    def send_feedback_to_publisher(self, params):
        #print('In send feedback to publisher function : ',params)
        self.pub.messageToTopic(params)
        pass # end of send_feedback_to_publisher function
    
    def update_log(self, params):
        self.ul = True
        self.ul_mesg = params
        pass # end of update_log function
    
    def log_box(self,_str):
        self.gui.txt_log.appendPlainText(_str)
        pass
    
    
    def load_data_to_gui(self):
        try:
            data = self.db.get_last_entry()
            if data[0] == 1:
                _imageName = data[1]
                _time = data[2]
                
                v = data[3]
                index = v.split('(')
                index = index[1].split(')')
                index = index[0].split(',')
                
                _width = int(index[0])
                _height = int(index[1])
                _expTime = data[4]
                _expMode = data[5]
                _wm = data[6]
                _iso = data[7]
                _brightness = data[8]
                _contrast = data[9]
                _saturation = data[10]
                _sharpness = data[11]
                
                _raw = data[12]
                
                self.gui.txt_fileName.setText(f'{_imageName}')
                self.gui.txt_imageWidth.setText(f'{str(_width)}')
                self.gui.txt_imageHeight.setText(f'{str(_height)}')
                
                self.gui.slider_expTime.setSliderPosition(int(_expTime))
                self.gui.slider_iso.setSliderPosition(int(_iso))
                self.gui.slider_brightness.setSliderPosition(int(_brightness))
                self.gui.slider_contrast.setSliderPosition(int(_contrast))
                self.gui.slider_saturation.setSliderPosition(int(_saturation ))
                self.gui.slider_sharpness.setSliderPosition(int(_sharpness))
                
                self.gui.cb_expMode.setCurrentText(f'{str(_expMode)}')
                self.gui.cb_whiteBalanceMode.setCurrentText(f'{str(_wm)}')
                self.gui.cb_raw.setCurrentText(f'{str(_raw)}')
                
        except Exception as error:
            print('Error in loading data to Gui : ',error)
        
        pass # end of load_data_to_gui() function
    
    def press_shoot(self):
        self.gui.params['imageName'] = self.gui.txt_fileName.text()
        self.gui.params['exposure_mode'] = self.gui.cb_expMode.currentText()
        self.gui.params['white_balance'] = self.gui.cb_whiteBalanceMode.currentText()
        self.gui.params['raw'] = self.gui.cb_raw.currentText()
        self.gui.params['time'] = get_now_string()
        try:
            
            self.Iwidth = int(self.gui.txt_imageWidth.text())
            self.Iheight = int(self.gui.txt_imageHeight.text()) 
            self.gui.params['resolution'] = (self.Iwidth, self.Iheight)
            self.gui.params['expose_time'] = int(self.gui.lbl_expTime.text())
            self.gui.params['iso'] = int(self.gui.lbl_iso.text())
            self.gui.params['brightness'] = int(self.gui.lbl_brightness.text())
            self.gui.params['contrast'] = int(self.gui.lbl_contrast.text())
            self.gui.params['saturation'] = int(self.gui.lbl_saturation.text())
            self.gui.params['sharpness'] = int(self.gui.lbl_sharpness.text())
            
            
        except Exception as err:
            print("ERROR : Formation Error, Please Enter correct format")
            self.log_box("ERROR : Formation Error, Please Enter correct format")
            
            return None
        if (len(self.gui.params['imageName']) > 0) and (len(str(self.Iwidth)) > 0) and (len(str(self.Iheight)) > 0):
            self.shoot = True
            self.pub.message(self.gui.params, self.path)
            
            pass
        else:
            self.log_box("Fill the empty Boxes")
      
            return None
        self.log_box("End Capturing...")
        
        pass # end of press_shoot function
    
    def update_cb_images(self, newstr):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        params = os.listdir(self.path)
        self.gui.cb_select_image.clear()
        for x in params:
            self.gui.cb_select_image.addItem(x)
            pass 
        pass #end of update_cb_images function 
    def stop(self):
        self.thread_loop = False
        self.join()
        pass # end of stop function
    
    def closeApp(self):
        self.thread_loop = False
        self.gui.close()
        self.exit()
        pass # end of closeApp() function
    def run(self):
        _in = ''
        _rpi_id = ''
        while self.thread_loop :
            self.gui.lbl_expTime.setText(str(self.gui.slider_expTime.value()))
            self.gui.lbl_iso.setText(str(self.gui.slider_iso.value()))
            self.gui.lbl_brightness.setText(str(self.gui.slider_brightness.value()))
            self.gui.lbl_contrast.setText(str(self.gui.slider_contrast.value()))
            self.gui.lbl_saturation.setText(str(self.gui.slider_saturation.value()))
            self.gui.lbl_sharpness.setText(str(self.gui.slider_sharpness.value()))
            
            if self.shoot == True:
                self.gui.txt_log.appendPlainText('Capturing Start')
                self.shoot = False
                
            if self.ul == True:
                self.gui.txt_log.appendPlainText(self.ul_mesg)
                self.ul = False
                pass
            pass # end of while loop
        pass # end of loop function
    pass # end of main class


def mainProg():
    app = QtWidgets.QApplication(sys.argv)
    controller = MAIN()
    controller.start()
    sys.exit(app.exec_())
    pass # end of mainProg
    
def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.MouseButtonRelease and obj.rect().contains(event.pos()):
                self.clicked.emit()
                return True
            else:
                return False
        pass # end of class filters

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

if __name__ == '__main__':
    mainProg()
    pass # end of main 
