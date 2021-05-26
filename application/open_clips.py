import sys
import os
import psutil

from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QApplication

from PyQt5.QtCore import QThread


class ClipsPage(QWidget):

    def __init__(self, parent=None):
        super(ClipsPage, self).__init__()
        self.padre = parent
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Learn a New Language")

        self.VBL = QVBoxLayout(self)

        self.FeedLabel = QLabel(self)
        self.VBL.addWidget(self.FeedLabel)

        self.Worker1 = Worker1()
        self.Worker1.start()
        self.setLayout(self.VBL)

    def closeEvent(self, event):
        """
        prompts a message box that states that the user is about to close live feed detection
        """
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close this window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.padre.toggle_buttons(True)
            event.accept()
            self.Worker1.stop()
            for process in (process for process in psutil.process_iter() if process.name() == "CLIPSIDE.exe"):
                process.kill()
            self.close()
        else:
            self.padre.test = False
            event.ignore()


class Worker1(QThread):
    def run(self):
        """
        starts the thread which captures live feed and sends the data to the
        algorithm for further analyzing
        """
        self.ThreadActive = True

        while self.ThreadActive:
            os.system(r'"D:/School/CLIPS/CLIPSIDE.exe"')

    def stop(self):
        """
        stops the thread
        :return:
        """
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = ClipsPage()
    Root.show()
    sys.exit(App.exec())
