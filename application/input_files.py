from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QFileDialog

from controller import PageWindow
from generator import FunctionalityGenerator, InputGenerator

from os.path import expanduser


class InputPage(PageWindow):

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
        self.label_1.setGeometry(QtCore.QRect(400, 110, 300, 50))
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(400, 360, 500, 50))
        self.label_2.setObjectName("label_2")

        self.layout_1 = QtWidgets.QGridLayout(self.label_1)
        self.setLayout(self.layout_1)

        self.layout_2 = QtWidgets.QGridLayout(self.label_2)
        self.setLayout(self.layout_2)

        self.radioButton_1 = QtWidgets.QRadioButton("Write Text")
        self.radioButton_1.choice = "Write"
        self.radioButton_1.toggled.connect(self.radio_event_1)
        self.layout_1.addWidget(self.radioButton_1, 0, 0)

        self.radioButton_2 = QtWidgets.QRadioButton("Upload File")
        self.radioButton_2.choice = "Upload"
        self.radioButton_2.toggled.connect(self.radio_event_2)
        self.layout_2.addWidget(self.radioButton_2, 0, 1)

        self.group = QtWidgets.QButtonGroup()
        self.group.addButton(self.radioButton_1)
        self.group.addButton(self.radioButton_2)

        self.path = QtWidgets.QLineEdit(self)
        self.path.setGeometry(QtCore.QRect(400, 420, 450, 30))
        self.path.setObjectName("path")
        self.path.setDisabled(True)
        self.path.setPlaceholderText("Path to the file to analyze...")

        self.path_1 = QtWidgets.QLineEdit(self)
        self.path_1.setGeometry(QtCore.QRect(400, 560, 450, 30))
        self.path_1.setObjectName("path_1")
        self.path_1.setDisabled(True)
        self.path_1.setPlaceholderText("Path to the directory to save...")

        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setGeometry(QtCore.QRect(850, 425, 40, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setDisabled(True)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.clicked.connect(self.browse_file_event)

        self.toolButton_1 = QtWidgets.QToolButton(self)
        self.toolButton_1.setGeometry(QtCore.QRect(850, 565, 40, 20))
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
        self.pushButton.setGeometry(QtCore.QRect(940, 730, 100, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.save_event)
        self.pushButton.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 730, 200, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_2.setObjectName("pushButton_1")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.clicked.connect(self.save_continue_event)
        self.pushButton_2.setDisabled(True)

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 730, 100, 50))
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_3.setObjectName("pushButton_1")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.clicked.connect(self.reset_event)
        self.pushButton_3.setDisabled(True)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(150, 110, 250, 50))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("INPUT DATA: ")
        self.label_4.setStyleSheet("font-size: 20px;")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(400, 155, 700, 150))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("background-color: rgb(220,220,220); border: 1px solid black;")
        self.label_5.setGraphicsEffect(self.shadow)

        self.layout_5 = QtWidgets.QGridLayout(self.label_5)
        self.setLayout(self.layout_5)

        self.textEdit = QtWidgets.QPlainTextEdit(self)
        self.layout_5.addWidget(self.textEdit)
        self.textEdit.setDisabled(True)
        self.textEdit.setPlaceholderText("Write your text here...")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(150, 550, 250, 50))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("SAVE DIRECTORY: ")
        self.label_6.setStyleSheet("font-size: 20px;")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("Dialog", "Back"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Save and Continue"))
        self.pushButton_3.setText(_translate("Dialog", "Reset"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton_1.setText(_translate("Dialog", "..."))

    def back_event(self):
        """
        on clicking the linked button, it opens the corresponding page and call for clearing the selections
        """
        self.goto('generate')

    def radio_event_1(self):
        self.toolButton.setDisabled(True)
        self.textEdit.setDisabled(False)
        self.check_for_save()

    def radio_event_2(self):
        if self.radioButton_2.isChecked():
            self.toolButton.setDisabled(False)
        self.check_for_save()

    def checkbox_event(self):
        self.check_for_save()

    def browse_file_event(self):
        """
        opens browser to choose path to image file
        """
        self.path.setText("")
        # opens a file dialog for the format
        file_path = QFileDialog.getOpenFileName(None, 'Select a file:', expanduser("~"),
                                                filter="All files (*.*);;RFT (*.rft);;APKG (*.apkg);;DOC (*.doc);;LST "
                                                       "(*.lst);;B (*.b);;FDR (*.fdr);;FCF (*.fcf);;TXT ("
                                                       "*.txt);;QBL (*.qbl);;ODM (*.odm);;LOG (*.log);;DOCX ("
                                                       "*.docx);;MAN (*.man);;OTT (*.ott);;ADOC (*.adoc);;SAVE ("
                                                       "*.save);;RTF (*.rtf);;DOCM (*.docm);;LTX (*.ltx);;TEXT ("
                                                       "*.text);; DAT (*.dat)")
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
        if ((self.path_1.text() != "" and self.path.text() != "")
                or (self.path_1.text() != "" and self.radioButton_1.isChecked())):
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(False)
        else:
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)
        if self.path_1.text() != "" or self.path.text() != "" or self.radioButton_1.isChecked() \
                or self.radioButton_2.isChecked() or self.checkBox_1.isChecked() or self.checkBox_2.isChecked():
            self.pushButton_3.setDisabled(False)
        else:
            self.pushButton_3.setDisabled(True)
        if self.radioButton_1.isChecked():
            self.textEdit.setDisabled(False)
        else:
            self.textEdit.setDisabled(True)

    def reset_event(self):
        self.path.setText("")
        self.path_1.setText("")
        # self.group.setExclusive(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_2.setChecked(False)
        # self.group.setExclusive(True)
        self.textEdit.setPlainText("")
        self.check_for_save()

    def save_event(self):
        self.save_functionality_files()
        self.goto('main')

    def save_functionality_files(self):
        text = self.get_text()

        ig = InputGenerator(text)
        text = ig.result

        with open(self.path_1.text()+"/input.dat", "w") as fout:
            fout.write(ig.result)

        self.message_box_saved()

    def save_continue_event(self):
        self.save_functionality_files()
        self.goto('functionalities')

    def get_text(self):
        if self.radioButton_1.isChecked() and self.textEdit.toPlainText() != "":
            return self.textEdit.toPlainText()
        if self.radioButton_2.isChecked():
            with open(self.path.text(), "r") as fin:
                text = fin.read()
                return text

    def message_box_saved(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(f"The file has been saved at {self.path_1.text()}")
        message_box.setWindowTitle("Saved")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()
