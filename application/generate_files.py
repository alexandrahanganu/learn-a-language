from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox

from controller import PageWindow
from open_clips import ClipsPage


class GenerateFilesPage(PageWindow):

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

        self.functionalities_button = QtWidgets.QPushButton(self)
        self.functionalities_button.setGeometry(QtCore.QRect(520, 140, 251, 151))
        self.functionalities_button.setObjectName("functionalities_button")

        self.input_button = QtWidgets.QPushButton(self)
        self.input_button.setGeometry(QtCore.QRect(520, 330, 251, 151))
        self.input_button.setObjectName("input_button")

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 730, 100, 50))
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.clicked.connect(self.back_event)

        self.retranslateUi()

        self.functionalities_button.clicked.connect(self.functionalities_event)
        self.input_button.clicked.connect(self.input_event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.functionalities_button.setText(_translate("MainWindow", "Generate Functionalities Files"))
        self.input_button.setText(_translate("MainWindow", "Generate Input Files"))
        self.pushButton_1.setText(_translate("Dialog", "Back"))

    def back_event(self):
        """
        on clicking the linked button, it opens the corresponding page and call for clearing the selections
        """
        self.goto('main')

    def functionalities_event(self):
        self.goto('functionalities')

    def input_event(self):
        self.goto('input')
