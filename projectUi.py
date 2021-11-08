# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog, QAction
from PyQt5.QtGui import QPixmap
from skimage import filters
from PIL import ImageQt
from PIL import Image as im
import cv2 
from skimage.morphology import thin
import numpy as np

class Ui_MainWindow(object):
    # class VideoThread(QThread):
    # change_pixmap_signal = pyqtSignal(np.ndarray)

    # def run(self):
    #     # capture from web cam
    #     cap = cv2.VideoCapture(0)
    #     while True:
    #         ret, cv_img = cap.read()
    #         if ret:
    #             self.change_pixmap_signal.emit(cv_img)


    path = ''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Computer Vision Project")
        MainWindow.resize(811, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filtersLabel = QtWidgets.QLabel(self.centralwidget)
        self.filtersLabel.setGeometry(QtCore.QRect(20, 90, 281, 20))
        self.filtersLabel.setObjectName("filtersLabel")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(20, 30, 131, 28))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(170, 30, 131, 28))
        self.saveButton.setObjectName("saveButton")
        self.filtrelerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.filtrelerComboBox.setGeometry(QtCore.QRect(20, 110, 281, 22))
        self.filtrelerComboBox.setObjectName("filtrelerComboBox")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.filtrelerComboBox.addItem("")
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(100, 140, 93, 28))
        self.applyButton.setObjectName("applyButton")
        self.histogramLabel = QtWidgets.QLabel(self.centralwidget)
        self.histogramLabel.setGeometry(QtCore.QRect(20, 190, 281, 20))
        self.histogramLabel.setObjectName("histogramLabel")
        self.histogramDisplayButton = QtWidgets.QPushButton(self.centralwidget)
        self.histogramDisplayButton.setGeometry(QtCore.QRect(20, 220, 141, 28))
        self.histogramDisplayButton.setObjectName("histogramDisplayButton")
        self.histogramThreshholdingButton = QtWidgets.QPushButton(self.centralwidget)
        self.histogramThreshholdingButton.setGeometry(QtCore.QRect(160, 220, 141, 28))
        self.histogramThreshholdingButton.setObjectName("histogramThreshholdingButton")
        self.spatialLabel = QtWidgets.QLabel(self.centralwidget)
        self.spatialLabel.setGeometry(QtCore.QRect(20, 270, 141, 20))
        self.spatialLabel.setObjectName("spatialLabel")
        self.spatialComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.spatialComboBox.setGeometry(QtCore.QRect(20, 290, 281, 22))
        self.spatialComboBox.setObjectName("spatialComboBox")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.exposureLabel = QtWidgets.QLabel(self.centralwidget)
        self.exposureLabel.setGeometry(QtCore.QRect(17, 360, 55, 16))
        self.exposureLabel.setObjectName("exposureLabel")
        self.exposure1Text = QtWidgets.QTextEdit(self.centralwidget)
        self.exposure1Text.setGeometry(QtCore.QRect(17, 380, 141, 21))
        self.exposure1Text.setObjectName("exposure1Text")
        self.exposure2Text = QtWidgets.QTextEdit(self.centralwidget)
        self.exposure2Text.setGeometry(QtCore.QRect(160, 380, 141, 21))
        self.exposure2Text.setObjectName("exposure2Text")
        self.morphologicalLabel = QtWidgets.QLabel(self.centralwidget)
        self.morphologicalLabel.setGeometry(QtCore.QRect(20, 460, 281, 16))
        self.morphologicalLabel.setObjectName("morphologicalLabel")
        self.morphologicalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.morphologicalComboBox.setGeometry(QtCore.QRect(20, 480, 281, 22))
        self.morphologicalComboBox.setObjectName("morphologicalComboBox")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")

        self.edgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.edgeLabel.setGeometry(QtCore.QRect(20, 560, 121, 16))
        self.edgeLabel.setObjectName("edgeLabel")
        self.videoButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoButton.setGeometry(QtCore.QRect(20, 580, 281, 28))
        self.videoButton.setObjectName("videoButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 471, 591))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 321, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 250, 321, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 350, 321, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 440, 321, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 540, 321, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(310, -10, 20, 651))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.exposureButton = QtWidgets.QPushButton(self.centralwidget)
        self.exposureButton.setGeometry(QtCore.QRect(20, 410, 281, 28))
        self.exposureButton.setObjectName("exposureButton")
        self.morphologicalButton = QtWidgets.QPushButton(self.centralwidget)
        self.morphologicalButton.setGeometry(QtCore.QRect(20, 510, 281, 28))
        self.morphologicalButton.setObjectName("morphologicalButton")
        self.spatialButton = QtWidgets.QPushButton(self.centralwidget)
        self.spatialButton.setGeometry(QtCore.QRect(20, 320, 281, 28))
        self.spatialButton.setObjectName("spatialButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadButton.clicked.connect(self.show_image)
        self.saveButton.clicked.connect(self.saveImage)
        # self.videoButton.clicked.connect(self.edgeDetection)
        self.morphologicalButton.clicked.connect(self.MorpOperations)
       ## self.applyButton.clicked.connect(self.filter)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filtersLabel.setText(_translate("MainWindow", "Filters"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.filtrelerComboBox.setItemText(0, _translate("MainWindow", "Gaussian"))
        self.filtrelerComboBox.setItemText(1, _translate("MainWindow", "Inverse"))
        self.filtrelerComboBox.setItemText(2, _translate("MainWindow", "Laplace"))
        self.filtrelerComboBox.setItemText(3, _translate("MainWindow", "Median"))
        self.filtrelerComboBox.setItemText(4, _translate("MainWindow", "Hessian"))
        self.filtrelerComboBox.setItemText(5, _translate("MainWindow", "Farid"))
        self.filtrelerComboBox.setItemText(6, _translate("MainWindow", "Roberts"))
        self.filtrelerComboBox.setItemText(7, _translate("MainWindow", "Otsu"))
        self.filtrelerComboBox.setItemText(8, _translate("MainWindow", "Sobel"))
        self.filtrelerComboBox.setItemText(9, _translate("MainWindow", "Sato"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.histogramLabel.setText(_translate("MainWindow", "Histogram display and thresholding"))
        self.histogramDisplayButton.setText(_translate("MainWindow", "Display"))
        self.histogramThreshholdingButton.setText(_translate("MainWindow", "Threshholding"))
        self.spatialLabel.setText(_translate("MainWindow", "Spatial transformations"))
        self.spatialComboBox.setItemText(0, _translate("MainWindow", "Resize"))
        self.spatialComboBox.setItemText(1, _translate("MainWindow", "Rotate"))
        self.spatialComboBox.setItemText(2, _translate("MainWindow", "Swirl"))
        self.spatialComboBox.setItemText(3, _translate("MainWindow", "Warp"))
        self.spatialComboBox.setItemText(4, _translate("MainWindow", "Crop"))
        self.exposureLabel.setText(_translate("MainWindow", "Exposure"))
        self.morphologicalLabel.setText(_translate("MainWindow", "Morphological Operations"))
        self.morphologicalComboBox.setItemText(0, _translate("MainWindow", "Erosion"))
        self.morphologicalComboBox.setItemText(1, _translate("MainWindow", "Dilation"))
        self.morphologicalComboBox.setItemText(2, _translate("MainWindow", "Opening"))
        self.morphologicalComboBox.setItemText(3, _translate("MainWindow", "Closing"))
        self.morphologicalComboBox.setItemText(4, _translate("MainWindow", "Cross"))
        self.morphologicalComboBox.setItemText(5, _translate("MainWindow", "Black Hat Transformation"))
        self.morphologicalComboBox.setItemText(6, _translate("MainWindow", "Top Hat Transformation"))
        self.morphologicalComboBox.setItemText(7, _translate("MainWindow", "Rectangle"))
        self.morphologicalComboBox.setItemText(8, _translate("MainWindow", "Morphological Gradient"))
        self.morphologicalComboBox.setItemText(9, _translate("MainWindow", "Ellipse"))

        self.edgeLabel.setText(_translate("MainWindow", "Edge Determination"))
        self.videoButton.setText(_translate("MainWindow", "Choose Video"))
        self.exposureButton.setText(_translate("MainWindow", "Exposure Apply"))
        self.morphologicalButton.setText(_translate("MainWindow", "Morphological Apply"))
        self.spatialButton.setText(_translate("MainWindow", "Spatial Apply"))


    def edge_detection(self,frame):
        if(len(frame.shape)==3):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        
        frame = cv2.Canny(frame, 30, 150)

        return frame
        
                
    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)



    def show_image(self):
        global path
        path, _ = QFileDialog.getOpenFileName()
        print(path)
        image = cv2.imread(path)
        image = QtGui.QImage(image, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def saveImage(self):
        image = ImageQt.fromqpixmap(self.label.pixmap())
        image.save('test.png')
    
    def MorpOperations(self):
        #base element for morp operations cases
        se_cv2 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        #Operations Case 
        if self.morphologicalComboBox.currentText() == 'Erosion':
            image = cv2.imread(path)
            erosion = cv2.erode(image, se_cv2, iterations=1)
            image = QtGui.QImage(erosion, erosion.shape[1], erosion.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Dilation':
            image = cv2.imread(path)
            dilate = cv2.dilate(image, se_cv2, iterations=1)
            image = QtGui.QImage(dilate, dilate.shape[1], dilate.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Opening':
            image = cv2.imread(path)
            open = cv2.morphologyEx(image, cv2.MORPH_OPEN, se_cv2)
            image = QtGui.QImage(open, open.shape[1], open.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Closing':
            image = cv2.imread(path)            
            close = cv2.morphologyEx(image, cv2.MORPH_CLOSE, se_cv2)
            image = QtGui.QImage(close, close.shape[1], close.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Cross':
            image = cv2.imread(path)
            cross = cv2.morphologyEx(image, cv2.MORPH_CROSS, se_cv2)
            image = QtGui.QImage(cross, cross.shape[1], cross.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Black Hat Transformation':
            image = cv2.imread(path)
            black = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, se_cv2)
            image = QtGui.QImage(black, black.shape[1], black.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Top Hat Transformation':
            image = cv2.imread(path)
            top = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, se_cv2)
            image = QtGui.QImage(top, top.shape[1], top.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Rectangle':
            image = cv2.imread(path)
            rect = cv2.morphologyEx(image, cv2.MORPH_RECT, se_cv2)
            image = QtGui.QImage(rect, rect.shape[1], rect.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))               

        elif self.morphologicalComboBox.currentText() == 'Morphological Gradient':
            image = cv2.imread(path)
            gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, se_cv2)
            image = QtGui.QImage(gradient, gradient.shape[1], gradient.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        elif self.morphologicalComboBox.currentText() == 'Ellipse':
            image = cv2.imread(path)
            ellipse = cv2.morphologyEx(image, cv2.MORPH_ELLIPSE, se_cv2)
            image = QtGui.QImage(ellipse, ellipse.shape[1], ellipse.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        else:
            pass

  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
