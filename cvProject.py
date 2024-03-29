# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog, QAction
from PyQt5.QtGui import QPixmap
from skimage import filters
from PIL import ImageQt
from PIL import Image as im

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filtersLabel = QtWidgets.QLabel(self.centralwidget)
        self.filtersLabel.setGeometry(QtCore.QRect(110, 90, 131, 20))
        self.filtersLabel.setObjectName("filtersLabel")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(20, 30, 131, 28))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(170, 30, 131, 28))
        self.saveButton.setObjectName("saveButton")
        self.filtrelerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.filtrelerComboBox.setGeometry(QtCore.QRect(90, 120, 101, 22))
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
        self.applyButton.setGeometry(QtCore.QRect(90, 160, 93, 28))
        self.applyButton.setObjectName("applyButton")
        self.histogramLabel = QtWidgets.QLabel(self.centralwidget)
        self.histogramLabel.setGeometry(QtCore.QRect(80, 220, 211, 16))
        self.histogramLabel.setObjectName("histogramLabel")
        self.histogramDisplayButton = QtWidgets.QPushButton(self.centralwidget)
        self.histogramDisplayButton.setGeometry(QtCore.QRect(40, 250, 93, 28))
        self.histogramDisplayButton.setObjectName("histogramDisplayButton")
        self.histogramThreshholdingButton = QtWidgets.QPushButton(self.centralwidget)
        self.histogramThreshholdingButton.setGeometry(QtCore.QRect(170, 250, 101, 28))
        self.histogramThreshholdingButton.setObjectName("histogramThreshholdingButton")
        self.spatialLabel = QtWidgets.QLabel(self.centralwidget)
        self.spatialLabel.setGeometry(QtCore.QRect(30, 310, 141, 20))
        self.spatialLabel.setObjectName("spatialLabel")
        self.spatialComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.spatialComboBox.setGeometry(QtCore.QRect(180, 310, 73, 22))
        self.spatialComboBox.setObjectName("spatialComboBox")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.spatialComboBox.addItem("")
        self.exposureLabel = QtWidgets.QLabel(self.centralwidget)
        self.exposureLabel.setGeometry(QtCore.QRect(30, 340, 55, 16))
        self.exposureLabel.setObjectName("exposureLabel")
        self.exposure1Text = QtWidgets.QTextEdit(self.centralwidget)
        self.exposure1Text.setGeometry(QtCore.QRect(20, 370, 104, 31))
        self.exposure1Text.setObjectName("exposure1Text")
        self.exposure2Text = QtWidgets.QTextEdit(self.centralwidget)
        self.exposure2Text.setGeometry(QtCore.QRect(150, 370, 104, 31))
        self.exposure2Text.setObjectName("exposure2Text")
        self.morphologicalLabel = QtWidgets.QLabel(self.centralwidget)
        self.morphologicalLabel.setGeometry(QtCore.QRect(60, 420, 151, 16))
        self.morphologicalLabel.setObjectName("morphologicalLabel")
        self.morphologicalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.morphologicalComboBox.setGeometry(QtCore.QRect(60, 450, 131, 22))
        self.morphologicalComboBox.setObjectName("morphologicalComboBox")
        self.morphologicalComboBox.addItem("")
        self.morphologicalComboBox.addItem("")
        self.edgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.edgeLabel.setGeometry(QtCore.QRect(60, 490, 121, 16))
        self.edgeLabel.setObjectName("edgeLabel")
        self.videoButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoButton.setGeometry(QtCore.QRect(60, 520, 93, 28))
        self.videoButton.setObjectName("videoButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 50, 331, 491))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.loadButton.clicked.connect(self.openImage)
        self.saveButton.clicked.connect(self.saveImage)
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
        self.edgeLabel.setText(_translate("MainWindow", "Edge Determination"))
        self.videoButton.setText(_translate("MainWindow", "Choose Video"))

    
    def openImage(self):
        global pixmap
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)

    def saveImage(self):
        image = ImageQt.fromqpixmap(self.label.pixmap())
        image.save('test.png')

   ## def filter(self):
        if self.filtrelerComboBox.currentText() == 'Sobel' :
            edges=filters.farid(pixmap)
            self.label.setPixmap(edges)
    
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
