import sys
import os
import pyttsx3
import time

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QStyle,
    QLabel,
    QSlider,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Tts:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.filepath = ""
    
    def save(self, text, file):
        self.filepath = file[0]
        self.engine.save_to_file(text, self.filepath)
        self.engine.runAndWait()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exsae Speak")
        self.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"assets/es.png"))
        
        #Text edit
        self.textEdit = QPlainTextEdit()

        #Save Button
        self.saveBtn = QPushButton(text="Save")
        self.saveBtn.clicked.connect(self.save)

        self.label = QLabel()

        #Initialize user interface
        self.init_ui()
    
    def init_ui(self):
        vlay = QVBoxLayout()
        vlay.addWidget(self.textEdit)
        vlay.addWidget(self.label)
        self.setLayout(vlay)

        hlay = QHBoxLayout()
        hlay.addWidget(self.saveBtn)
        vlay.addLayout(hlay)
    
    def save(self):
        if self.textEdit.toPlainText() != "":
            self.saveBtn.setEnabled(False)
            file = QFileDialog.getSaveFileName(None, "Save to audio file", filter="*.mp3")
            tts = Tts()
            tts.save(self.textEdit.toPlainText(), file)
            self.textEdit.setPlainText("")
            self.saveBtn.setEnabled(True)
            self.label.setText("")
        else:
            self.label.setText("No text to read!")


app = QApplication(sys.argv)
style = """
Window {
    background-color: rgb(225,225,225);
}

QPlainTextEdit {
    border: none;
}
"""
app.setStyleSheet(style)
window = Window()
window.show()
sys.exit(app.exec_())