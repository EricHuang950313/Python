import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tutorial a.py")
        self.setWindowIcon(QIcon("./PyQt.png"))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        button = QPushButton("Say Hello", clicked=self.sayHello)
        button.clicked.connect(self.sayHello)

        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)


    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText("Hello"+inputText)



if __name__ == "__main__":
    gui = QApplication(sys.argv)
    window = myApp()
    window.show()
    gui.exec()
