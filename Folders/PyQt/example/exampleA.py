from PyQt6.QtWidgets import *
import exampleA_module as igui

class Main(QMainWindow, igui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from designer.
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    gui = QApplication(sys.argv)
    widget = Main()
    widget.setWindowTitle("exampleA.py")
    widget.show()
    sys.exit(gui.exec())