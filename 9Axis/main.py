from PyQt5.QtWidgets import QApplication
import sys
from display import DisplayParts



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DisplayParts()
    win.show()

    app.exec()