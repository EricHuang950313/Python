import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standard Calculator Ver0.5")
        self.setWindowIcon(QIcon("./Calculator.jpg"))

if __name__ == "__main__":
    gui = QApplication(sys.argv)
    window = myApp()
    window.show()
    gui.exec()
