import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exsae Speak")
        self.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"assets/es.png"))


app = QApplication(sys.argv)
style = """
Window {
    background-color: blue;
}
"""
app.setStyleSheet(style)
window = Window()
window.show()
sys.exit(app.exec_())