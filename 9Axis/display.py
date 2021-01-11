from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from GUI import Ui_MainWindow

class DisplayParts(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DisplayParts, self).__init__()
        self.setupUi(self)
        self.MoveCenter()

        lcd1 = self.lcdNumber
        lcd2 = self.lcdNumber_2
        lcd3 = self.lcdNumber_3
        lcd4 = self.lcdNumber_4
        lcd5 = self.lcdNumber_5
        lcd6 = self.lcdNumber_6
        lcd7 = self.lcdNumber_7
        lcd8 = self.lcdNumber_8
        lcd9 = self.lcdNumber_9

        self.lcd = [[lcd1, lcd2, lcd3], [lcd4, lcd5, lcd6], [lcd7, lcd8, lcd9]]

    def MoveCenter(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), int((screen.height() - size.height())/2) - 30)
