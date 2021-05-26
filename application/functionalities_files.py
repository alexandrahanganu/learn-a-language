from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QFileDialog

from controller import PageWindow

from os.path import expanduser


class FunctionalitiesPage(PageWindow):

    def __init__(self):
        super().__init__()
        self.ok = 1
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Learn a New Language")

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        # frame that contains all elements:
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(400, 110, 300, 100))
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(400, 260, 1000, 100))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(400, 310, 1000, 100))
        self.label_3.setObjectName("label_2")

        self.layout_1 = QtWidgets.QGridLayout(self.label_1)
        self.setLayout(self.layout_1)

        self.radioButton_1 = QtWidgets.QRadioButton("Default")
        self.radioButton_1.choice = "Default"
        self.radioButton_1.toggled.connect(self.radio_event_1)
        self.layout_1.addWidget(self.radioButton_1, 0, 0)

        self.radioButton_2 = QtWidgets.QRadioButton("Custom")
        self.radioButton_2.choice = "Custom"
        self.radioButton_2.toggled.connect(self.radio_event_2)
        self.layout_1.addWidget(self.radioButton_2, 0, 1)

        self.layout_2 = QtWidgets.QGridLayout(self.label_2)
        self.setLayout(self.layout_2)

        self.layout_3 = QtWidgets.QGridLayout(self.label_3)
        self.setLayout(self.layout_3)

        self.checkBox_1 = QtWidgets.QCheckBox()
        self.checkBox_1.choice = "Learn or Update"
        self.checkBox_1.toggled.connect(self.onClicked)
        self.layout_2.addWidget(self.checkBox_1)

        self.checkBox_2 = QtWidgets.QCheckBox()
        self.checkBox_2.choice = "Parse"
        self.checkBox_2.toggled.connect(self.onClicked)
        self.layout_3.addWidget(self.checkBox_2)

        self.path = QtWidgets.QLineEdit(self)
        self.path.setGeometry(QtCore.QRect(570, 180, 450, 30))
        self.path.setObjectName("path")
        self.path.setDisabled(True)
        self.path.setPlaceholderText("Path to the file to analyze...")

        self.path_1 = QtWidgets.QLineEdit(self)
        self.path_1.setGeometry(QtCore.QRect(300, 630, 450, 30))
        self.path_1.setObjectName("path_1")
        self.path_1.setDisabled(True)
        self.path_1.setPlaceholderText("Path to the directory to save...")

        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setGeometry(QtCore.QRect(1040, 185, 40, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setDisabled(True)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.clicked.connect(self.browse_file_event)

        self.toolButton_1 = QtWidgets.QToolButton(self)
        self.toolButton_1.setGeometry(QtCore.QRect(900, 640, 40, 20))
        self.toolButton_1.setObjectName("toolButton_1")
        self.toolButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_1.clicked.connect(self.browse_directory_event)

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 730, 100, 50))
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.clicked.connect(self.back_event)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(1040, 730, 100, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.save_event)
        self.pushButton.setDisabled(True)

        self.retranslateUi()
        #
        # self.functionalities_button.clicked.connect(self.functionalities_event)
        # self.input_button.clicked.connect(self.input_event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("Dialog", "Back"))
        self.checkBox_1.setText(_translate("Dialog", "Learning or Updating a Grammar"))
        self.checkBox_2.setText(_translate("Dialog", "Parsing the Input Sentences"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton_1.setText(_translate("Dialog", "..."))

    def back_event(self):
        """
        on clicking the linked button, it opens the corresponding page and call for clearing the selections
        """
        self.goto('generate')

    def functionalities_event(self):
        self.goto('functionalities')

    def input_event(self):
        self.goto('input')

    def radio_event_1(self):
        self.toolButton.setDisabled(True)
        if not self.radioButton_2.isChecked():
            pass

    def radio_event_2(self):
        if self.radioButton_2.isChecked():
            self.toolButton.setDisabled(False)

    def onClicked(self):
        pass

    def browse_file_event(self):
        """
        opens browser to choose path to image file
        """
        self.path.setText("")
        # opens a file dialog for the format
        file_path = QFileDialog.getOpenFileName(None, 'Select a file:', expanduser("~"),
                                                filter="All files (*.*);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS "
                                                       "(*.icns);;ICO (*.ico);;JPEG (*.jpeg);;JPG (*.jpg);;PBM ("
                                                       "*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG ("
                                                       "*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF ("
                                                       "*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM ("
                                                       "*.xpm)")
        self.path.setText(file_path[0])
        self.check_for_save()

    def browse_directory_event(self):
        """
        opens browser to choose path to folder to save image
        """
        self.path_1.setText("")
        directory_path = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.path_1.setText(directory_path)
        self.check_for_save()

    def check_for_save(self):
        """
        enables/disables the save button depending on whether the paths are filled or not
        """
        if self.path_1.text() != "" and self.path.text() != "":
            self.pushButton.setDisabled(False)
        else:
            self.pushButton.setDisabled(True)

    def save_event(self):
        """
        gets the image from the path, applies the algorithm and then saves the annotated picture
        """
        pass
