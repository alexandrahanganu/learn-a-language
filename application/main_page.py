from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controller import PageWindow
from open_clips import ClipsPage


class MainPage(PageWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Learn a Language")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        # frame that contains all elements:
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 310, 700, 150))
        self.label.setStyleSheet("QLabel{background-image: url(./images/image.png) 0 0 0 0 stretch stretch;}")
        self.label.setObjectName("label")

        self.picture_button = QtWidgets.QPushButton(self)
        self.picture_button.setGeometry(QtCore.QRect(820, 140, 251, 151))
        self.picture_button.setObjectName("picture_button")

        self.clips_button = QtWidgets.QPushButton(self)
        self.clips_button.setGeometry(QtCore.QRect(820, 330, 251, 151))
        self.clips_button.setObjectName("clips_button")

        self.info_button = QtWidgets.QPushButton(self)
        self.info_button.setGeometry(QtCore.QRect(820, 500, 251, 151))
        self.info_button.setObjectName("info_button")

        self.retranslateUi()

        self.picture_button.clicked.connect(self.picture_event)
        self.clips_button.clicked.connect(self.clips_event)
        self.info_button.clicked.connect(self.info_event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.picture_button.setText(_translate("MainWindow", "Generate CLIPS Files"))
        self.clips_button.setText(_translate("MainWindow", "Open CLIPS IDE"))
        self.info_button.setText(_translate("MainWindow", "About"))

    def picture_event(self):
        """
        on clicking the linked button, it opens the corresponding page
        """
        self.goto('generate')

    def clips_event(self):
        """
        on clicking the linked button, it opens the message box
        """
        self.message_box_clips()

    def message_box_clips(self):
        """
        prompts a message box that states that the user is about to open live feed detection
        """
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText("You are about to open a new page for the CLIPS IDE."
                            "\nDo you wish to continue?")
        message_box.setWindowTitle("Information")
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.buttonClicked.connect(self.message_box_button_clicked)
        message_box.exec_()

    def message_box_button_clicked(self, i):
        """
        when the OK button is clicked, a new instance of LivePage() is created
        """
        if i.text() == "OK":
            self.widget = ClipsPage(self)
            self.widget.setHidden(False)
            self.toggle_buttons(False)

    def toggle_buttons(self, status):
        """
        sets to hidden all fields until the LivePage() is closed
        """
        self.picture_button.setHidden(True ^ status)
        self.info_button.setHidden(True ^ status)
        self.clips_button.setHidden(True ^ status)
        self.label.setHidden(True ^ status)

    def info_event(self):
        """
        on clicking the linked button, it opens the corresponding page
        """
        self.goto('about')
