import os
import win32gui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox, QWindow
from caiji_thread import ContentCaiji
from utils import remove_images

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hwnd1 = win32gui.FindWindowEx(0, 0, "Messiah_Game", "一梦江湖")
        self.resize(1280, 780)
        self.setWindowTitle('一梦江湖-采集')
        window = QWindow.fromWinId(hwnd1)
        self.btn = QPushButton("开始采集")
        self.btn1 = QPushButton('停止采集')
        self.layout_h = QVBoxLayout()
        self.btn.clicked.connect(self.caiji_start)
        self.btn1.clicked.connect(self.caiji_stop)
        widget = self.createWindowContainer(window, self)
        self.layout_w = QHBoxLayout()
        self.layout_w.addWidget(self.btn)
        self.layout_w.addWidget(self.btn1)
        self.layout_h.addLayout(self.layout_w)
        self.layout_h.addWidget(widget)
        self.setLayout(self.layout_h)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', '确认退出?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            remove_images()
            os.system("taskkill /F /IM wyclx64.exe")
        else:
            event.ignore()

    def caiji_start(self):
        self.thread1 = ContentCaiji()
        self.thread1.start()

    def caiji_stop(self):
        self.thread1.terminate()
        remove_images()
