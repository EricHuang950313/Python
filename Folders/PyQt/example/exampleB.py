import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    # A-Create an application object.
    # print(sys.argv) result: ['exampleB.py']
    gui = QApplication(sys.argv)
    # B-"QWidget()" is a base class of all user interface objects in PyQt6.
    widget = QWidget()
    # C-Set the title of the application.
    widget.setWindowTitle("exampleB.py")
    # D-Displays the widget on the screen.
    widget.show()
    # E-"gui.exec()" enters the mainloop of the application. "sys.exit" method ensures a clean exit.
    sys.exit(gui.exec())


if __name__ == "__main__":
    main()