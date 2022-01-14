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
#from scipy.ndimage import imread

class GUI(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        # set exposure time slider
        self.slider_expTime.setMaximum(10)
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
    
    def load_image(self, image_name):
        input_image = Image.open(image_name)#imread(image_name)
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
        pass # end of load image function
        
        
    pass


class MAIN(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_loop = True
        # RPi ID , should be unique
        self.gui = GUI()
        self.gui.show()
        RPI_ID = 3
        server = "192.168.10.11"
        port = 1883
        
        self.path = 'Images/'
        self.ImageName = ''
        self.Iwidth = 100
        self.Iheight = 100
        
        # init rpi as publisher with unique id (used in MQTT topic)
        self.pub = Pub(RPI_ID, server, port)
        
        # init rpi as subscriber to subscripbe all rpi's in define MQTT topic
        self.sub = Sub(server, port, self.path)
        
        # set booleans for GUI Int
        self.shoot = False
        self.load_images = False
        
        try:
            self.gui.load_image(f'{self.path}test.png')
        except:
            pass
        #clickable(self.txtPassword).connect(self.presstxt_password)
        self.gui.btn_shoot.clicked.connect(lambda: self.press_shoot())
        
        pass # end of main __init__ function
    def press_shoot(self):
        
        self.shoot = True
        self.gui.params['imageName'] = self.gui.txt_fileName.text()
        self.gui.params['exposure_mode'] = self.gui.cb_expMode.currentText()
        self.gui.params['white_balance'] = self.gui.cb_whiteBalanceMode.currentText()
        self.gui.params['raw'] = self.gui.cb_raw.currentText()
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
            self.shoot = False
            return None
        if (len(self.gui.params['imageName']) > 0) and (len(str(self.Iwidth)) > 0) and (len(str(self.Iheight)) > 0):
            self.pub.message(self.gui.params, self.path)
            self.shoot = False
            pass
        else:
            print('Fill the empty Boxes')
            self.shoot= False
            return None
        
        pass # end of press_shoot function
    def stop(self):
        self.thread_loop = False
        self.join()
        pass # end of stop function
        
    def run(self):
        while self.thread_loop :
            self.gui.lbl_expTime.setText(str(self.gui.slider_expTime.value()))
            self.gui.lbl_iso.setText(str(self.gui.slider_iso.value()))
            self.gui.lbl_brightness.setText(str(self.gui.slider_brightness.value()))
            self.gui.lbl_contrast.setText(str(self.gui.slider_contrast.value()))
            self.gui.lbl_saturation.setText(str(self.gui.slider_saturation.value()))
            self.gui.lbl_sharpness.setText(str(self.gui.slider_sharpness.value()))
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
