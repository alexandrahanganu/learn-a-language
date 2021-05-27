from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from main_page import MainPage
from generate_files import GenerateFilesPage
from about_page import AboutPage
from controller import PageWindow
from functionalities_files import FunctionalitiesPage
from input_files import InputPage


class Window(QtWidgets.QMainWindow, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.m_pages = {}
        self.register(MainPage(), "main")
        self.register(GenerateFilesPage(), "generate")
        self.register(FunctionalitiesPage(), "functionalities")
        self.register(InputPage(), "input")
        self.register(AboutPage(), "about")
        self.goto("main")
        PageWindow.add_fonts(self)

    def register(self, widget, name):
        """
        adds the widgets and their respective names in the stack so that they can be used later when commuting from one
        page to another (from widget to widget)
        """
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.setFixedSize(1300, 800)
    w.show()
    sys.exit(app.exec_())
