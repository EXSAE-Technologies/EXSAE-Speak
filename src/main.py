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
    
    def change_rate(self, rate=180):
        self.engine.setProperty('rate', rate)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exsae Speak")
        self.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"assets/es.png"))

        self.tts = Tts()
        self.tts.change_rate(rate=160)
        
        #Text edit
        self.textEdit = QPlainTextEdit()

        #Save Button
        self.saveBtn = QPushButton(text="Save to Mp3")
        self.saveBtn.clicked.connect(self.save)

        #Run Test Button
        self.testBtn = QPushButton(text="Run Test")
        self.testBtn.clicked.connect(self.run_test_speech)

        self.label = QLabel()

        #Slider
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(30, 240)
        self.slider.setValue(160)
        self.slider.valueChanged.connect(self.slider_value_changed)

        self.sliderMin = QLabel(text=str(self.slider.value()))
        self.sliderMax = QLabel(text="240")

        #Initialize user interface
        self.init_ui()
    
    def init_ui(self):
        vlay = QVBoxLayout()
        vlay.addWidget(self.textEdit)
        vlay.addWidget(self.label)
        self.setLayout(vlay)

        hlays = QHBoxLayout()
        hlays.addWidget(self.sliderMin)
        hlays.addWidget(self.slider)
        hlays.addWidget(self.sliderMax)
        vlay.addLayout(hlays)

        hlay = QHBoxLayout()
        hlay.addWidget(self.saveBtn)
        hlay.addWidget(self.testBtn)
        vlay.addLayout(hlay)
    
    def save(self):
        if self.textEdit.toPlainText() != "":
            self.saveBtn.setEnabled(False)
            file = QFileDialog.getSaveFileName(None, "Save to audio file", filter="*.mp3")
            self.tts.save(self.textEdit.toPlainText(), file)
            self.textEdit.setPlainText("")
            self.saveBtn.setEnabled(True)
            self.label.setText("")
        else:
            self.label.setText("No text to read!")
    
    def slider_value_changed(self, value):
        self.sliderMin.setText(str(value))
        self.tts.change_rate(value)
    
    def run_test_speech(self):
        self.saveBtn.setEnabled(False)
        self.testBtn.setEnabled(False)
        self.slider.setEnabled(False)
        text = "The quick brown fox jumps over the lazy dog."
        self.tts.engine.say(text)
        self.tts.engine.runAndWait()
        self.saveBtn.setEnabled(True)
        self.testBtn.setEnabled(True)
        self.slider.setEnabled(True)


app = QApplication(sys.argv)
style = """
Window {
    background-color: rgb(225,225,225);
}

QPlainTextEdit {
    border: none;
    color: rgb(0,110,110);
}

QPushButton {
    background-color: rgb(50,100,100);
    color: white;
}
QPushButton:hover {
    background-color: white;
    color: rgb(0,110,110);
}
"""
app.setStyleSheet(style)
window = Window()
window.show()
sys.exit(app.exec_())