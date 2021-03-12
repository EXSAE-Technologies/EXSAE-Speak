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
    
    def save(self, text):
        filename = 'data'+os.path.sep+'saved-'+str(time.time())+'.mp3'
        filepath = os.path.dirname(__file__)+os.path.sep+filename
        self.engine.save_to_file(text, filepath)
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

        #open button
        self.open = QPushButton(text="Open")
        self.open.clicked.connect(self.open_file)

        #play Button
        self.play = QPushButton()
        self.play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        #Player button
        self.playerBtn = QPushButton(text="Player")

        #Slider
        self.slider = QSlider(orientation=Qt.Horizontal)

        #Media Player
        self.mediaPlayer = QMediaPlayer()

        #Initialize user interface
        self.init_ui()
    
    def init_ui(self):
        vlay = QVBoxLayout()
        vlay.addWidget(self.textEdit)
        vlay.addWidget(self.slider)
        self.setLayout(vlay)

        hlay = QHBoxLayout()
        hlay.addWidget(self.saveBtn)
        hlay.addWidget(self.open)
        vlay.addLayout(hlay)
    
    def save(self):
        self.saveBtn.setEnabled(False)
        tts = Tts()
        tts.save(self.textEdit.toPlainText())
        self.textEdit.setPlainText("")
        self.saveBtn.setEnabled(True)
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileUrl(None, filter="*.mp3")
        print(filename)


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