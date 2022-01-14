from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox
import sys
from PyQt5.QtGui import QIcon, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 543)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:1, stop:0 rgba(146, 146, 146, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_iso = QtWidgets.QSlider(self.centralwidget)
        self.slider_iso.setGeometry(QtCore.QRect(330, 290, 391, 22))
        self.slider_iso.setAutoFillBackground(False)
        self.slider_iso.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_iso.setOrientation(QtCore.Qt.Horizontal)
        self.slider_iso.setObjectName("slider_iso")
        self.txt_fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_fileName.setGeometry(QtCore.QRect(330, 40, 391, 41))
        self.txt_fileName.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";")
        self.txt_fileName.setText("")
        self.txt_fileName.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_fileName.setObjectName("txt_fileName")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 400, 191, 41))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_9.setObjectName("label_9")
        self.slider_sharpness = QtWidgets.QSlider(self.centralwidget)
        self.slider_sharpness.setGeometry(QtCore.QRect(330, 450, 391, 22))
        self.slider_sharpness.setAutoFillBackground(False)
        self.slider_sharpness.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_sharpness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_sharpness.setObjectName("slider_sharpness")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 131, 41))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 280, 131, 41))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_8.setObjectName("label_8")
        self.lbl_sharpness = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sharpness.setGeometry(QtCore.QRect(740, 450, 61, 16))
        self.lbl_sharpness.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_sharpness.setObjectName("lbl_sharpness")
        self.slider_saturation = QtWidgets.QSlider(self.centralwidget)
        self.slider_saturation.setGeometry(QtCore.QRect(330, 410, 391, 22))
        self.slider_saturation.setAutoFillBackground(False)
        self.slider_saturation.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturation.setObjectName("slider_saturation")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 141, 41))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.lbl_saturation = QtWidgets.QLabel(self.centralwidget)
        self.lbl_saturation.setGeometry(QtCore.QRect(740, 410, 61, 16))
        self.lbl_saturation.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_saturation.setObjectName("lbl_saturation")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.btn_exit.setStyleSheet("background-color: black;\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 5px;")
        self.btn_exit.setObjectName("btn_exit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 131, 41))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.cb_select_image = QtWidgets.QComboBox(self.centralwidget)
        self.cb_select_image.setGeometry(QtCore.QRect(840, 310, 241, 41))
        self.cb_select_image.setStyleSheet("background-color: rgba(107, 107, 107, 0.3); color: rgb(255,255,255);")
        self.cb_select_image.setObjectName("cb_select_image")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 370, 151, 20))
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_10.setObjectName("label_10")
        self.cb_whiteBalanceMode = QtWidgets.QComboBox(self.centralwidget)
        self.cb_whiteBalanceMode.setGeometry(QtCore.QRect(420, 240, 241, 41))
        self.cb_whiteBalanceMode.setStyleSheet("background-color: rgba(107, 107, 107, 0.3); color: rgb(255,255,255);")
        self.cb_whiteBalanceMode.setObjectName("cb_whiteBalanceMode")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 131, 20))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.txt_imageWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_imageWidth.setGeometry(QtCore.QRect(330, 80, 391, 41))
        self.txt_imageWidth.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";")
        self.txt_imageWidth.setText("")
        self.txt_imageWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_imageWidth.setObjectName("txt_imageWidth")
        self.lbl_Image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Image.setGeometry(QtCore.QRect(920, 360, 261, 161))
        self.lbl_Image.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(94, 113, 177);\n"
"")
        self.lbl_Image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_Image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_Image.setText("")
        self.lbl_Image.setObjectName("lbl_Image")
        self.slider_contrast = QtWidgets.QSlider(self.centralwidget)
        self.slider_contrast.setGeometry(QtCore.QRect(330, 370, 391, 22))
        self.slider_contrast.setAutoFillBackground(False)
        self.slider_contrast.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contrast.setObjectName("slider_contrast")
        self.txt_log = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_log.setGeometry(QtCore.QRect(840, 40, 411, 261))
        self.txt_log.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";")
        self.txt_log.setObjectName("txt_log")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 320, 131, 41))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.lbl_iso = QtWidgets.QLabel(self.centralwidget)
        self.lbl_iso.setGeometry(QtCore.QRect(740, 290, 61, 16))
        self.lbl_iso.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_iso.setObjectName("lbl_iso")
        self.cb_raw = QtWidgets.QComboBox(self.centralwidget)
        self.cb_raw.setGeometry(QtCore.QRect(420, 480, 241, 41))
        self.cb_raw.setStyleSheet("background-color: rgba(107, 107, 107, 0.3); color: rgb(255,255,255);")
        self.cb_raw.setObjectName("cb_raw")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 210, 151, 20))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.slider_brightness = QtWidgets.QSlider(self.centralwidget)
        self.slider_brightness.setGeometry(QtCore.QRect(330, 330, 391, 22))
        self.slider_brightness.setAutoFillBackground(False)
        self.slider_brightness.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brightness.setObjectName("slider_brightness")
        self.slider_expTime = QtWidgets.QSlider(self.centralwidget)
        self.slider_expTime.setGeometry(QtCore.QRect(330, 170, 391, 22))
        self.slider_expTime.setAutoFillBackground(False)
        self.slider_expTime.setStyleSheet("background-color: rgba(20, 89, 132,0.0);\n"
"")
        self.slider_expTime.setOrientation(QtCore.Qt.Horizontal)
        self.slider_expTime.setObjectName("slider_expTime")
        self.lbl_contrast = QtWidgets.QLabel(self.centralwidget)
        self.lbl_contrast.setGeometry(QtCore.QRect(740, 370, 61, 16))
        self.lbl_contrast.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_contrast.setObjectName("lbl_contrast")
        self.btn_loadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadImage.setGeometry(QtCore.QRect(1090, 310, 161, 41))
        self.btn_loadImage.setStyleSheet("background-color: black;\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 5px;")
        self.btn_loadImage.setObjectName("btn_loadImage")
        self.btn_shoot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_shoot.setGeometry(QtCore.QRect(20, 50, 141, 151))
        self.btn_shoot.setStyleSheet("background-color: rgb(20, 89, 132);\n"
"color:rgb(255, 255, 255);\n"
"font: 16pt \"Franklin Gothic Heavy\";\n"
"border-radius: 5px;")
        self.btn_shoot.setObjectName("btn_shoot")
        self.lbl_expTime = QtWidgets.QLabel(self.centralwidget)
        self.lbl_expTime.setGeometry(QtCore.QRect(730, 170, 61, 16))
        self.lbl_expTime.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_expTime.setObjectName("lbl_expTime")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 440, 131, 41))
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_11.setObjectName("label_11")
        self.cb_expMode = QtWidgets.QComboBox(self.centralwidget)
        self.cb_expMode.setGeometry(QtCore.QRect(420, 200, 241, 41))
        self.cb_expMode.setStyleSheet("background-color: rgba(107, 107, 107, 0.3); color: rgb(255,255,255);")
        self.cb_expMode.setObjectName("cb_expMode")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 240, 191, 41))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_7.setObjectName("label_7")
        self.txt_imageHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_imageHeight.setGeometry(QtCore.QRect(330, 120, 391, 41))
        self.txt_imageHeight.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";")
        self.txt_imageHeight.setText("")
        self.txt_imageHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_imageHeight.setObjectName("txt_imageHeight")
        self.lbl_brightness = QtWidgets.QLabel(self.centralwidget)
        self.lbl_brightness.setGeometry(QtCore.QRect(740, 330, 61, 16))
        self.lbl_brightness.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0.0);")
        self.lbl_brightness.setObjectName("lbl_brightness")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(190, 480, 131, 41))
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0, x2:0.443182, y2:0.988636, stop:1 rgba(201, 201, 201, 0));\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_12.setObjectName("label_12")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Saturation"))
        self.label_2.setText(_translate("MainWindow", "Image Width"))
        self.label_8.setText(_translate("MainWindow", "ISO"))
        self.lbl_sharpness.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Exposure Time"))
        self.lbl_saturation.setText(_translate("MainWindow", "0"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Image Height"))
        self.label_10.setText(_translate("MainWindow", "Contrast"))
        self.label.setText(_translate("MainWindow", "Filename Base"))
        self.label_6.setText(_translate("MainWindow", "Brightness"))
        self.lbl_iso.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Exposure Mode"))
        self.lbl_contrast.setText(_translate("MainWindow", "0"))
        self.btn_loadImage.setText(_translate("MainWindow", "Open Image"))
        self.btn_shoot.setText(_translate("MainWindow", "SHOOT"))
        self.lbl_expTime.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Sharpness"))
        self.label_7.setText(_translate("MainWindow", "White Balance Mode"))
        self.lbl_brightness.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Output raw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

