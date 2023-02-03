# -*- encoding=utf8 -*-
__author__ = "xiaoqidao"

from airtest.core.api import *

auto_setup(__file__)

import random
import base64
from image import img1,img2,img3,img4
import time
import cv2
import win32con
import win32ui
import win32api
import ctypes
import time
import sys
import win32gui
from PyQt5.QtGui import QFont  # QtWidgets不包含QFont必须调用QtGui
from PyQt5.QtGui import QWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout


class content_caiji(QThread):
    def __init__(self):
        super().__init__()
        if win32gui.FindWindow(None, '一梦江湖-采集') == 0:
            pass
        else:
            self.hwnd = win32gui.FindWindow(None, '一梦江湖-采集')
            self.hwndChildList = []  # 创建子窗口列表
            win32gui.EnumChildWindows(self.hwnd, lambda hwnd, param: param.append(self.hwnd), self.hwndChildList)
            self.hwnd1 = win32gui.FindWindowEx(self.hwndChildList[0], 0, None, None)
            #             title = win32gui.GetWindowText(self.hwnd1)
            #             print(('窗口标题:%s' % (title) )+ '  '+str(title))
            #             title = win32gui.GetWindowText(self.hwndChildList[0])
            #             print(('窗口标题:%s' % (title) )+ '  '+str(title))
            auto_setup(__file__, devices=["Windows:///" + str(self.hwnd1)])

    def pc_clicked(self, coordinate):
        tmp = coordinate
        tmp = win32api.MAKELONG(int(tmp[0]), int(tmp[1]))
        win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)  # 鼠标左键按下
        win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)  # 鼠标左键抬起

    def run(self, r=100, w=0):
        os.mkdir("image")
        tmp1 = open('image/tpl1675244038936.png', 'wb')
        tmp1.write(base64.b64decode(img1))
        tmp1.close()
        tmp2 = open('image/tpl1675244201268.png', 'wb')
        tmp2.write(base64.b64decode(img2))
        tmp2.close()
        tmp3 = open('image/tpl1675395304672.png', 'wb')
        tmp3.write(base64.b64decode(img3))
        tmp3.close()
        tmp3 = open('image/tpl1675396178938.png', 'wb')
        tmp3.write(base64.b64decode(img4))
        tmp3.close()
        b = 0
        while (b < r):
            if (exists(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105), resolution=(1175, 789))) != False):
                print('开始采集')
                self.pc_clicked(
                    exists(Template(r"image/tpl1675244201268.png", record_pos=(0.344, 0.105), resolution=(1162, 789))))
                while (True):
                    print('正在检测采集进度')

                    if (exists(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105),
                                        resolution=(1175, 789))) == False):
                        break
                    sleep(0.5)

            else:
                wait(Template(r"image/tpl1675395304672.png", threshold=0.8, record_pos=(0.383, -0.232),
                              resolution=(1170, 638)))
                tmp = exists(Template(r"image/tpl1675395304672.png", threshold=0.8, record_pos=(0.383, -0.232),
                                      resolution=(1170, 638)))
                tmp = win32api.MAKELONG(int(tmp[0]), int(tmp[1]))
                win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)  # 鼠标左键按下
                win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)  # 鼠标左键抬起
                if (((w + 1) % 4) == 0):
                    w = 0
                else:
                    d = random.randint(1, 5 - w)
                    huanxian = exists(
                        Template(r"image/tpl1675396178938.png", record_pos=(0.275, -0.215), resolution=(1170, 638)))

                    tmp = [int(huanxian[0]), int(round(huanxian[1] * d))]
                    tmp = win32api.MAKELONG(tmp[0], tmp[1])
                    win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)  # 鼠标左键按下
                    win32gui.PostMessage(self.hwnd1, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)  # 鼠标左键抬起
                    w += 1
                    wait(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105), resolution=(1175, 789)))
                    sleep(1)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        hwnd1 = win32gui.FindWindowEx(0, 0, "Messiah_Game", "一梦江湖")  # 微信窗口的类名和标题
        self.resize(1280, 780)
        self.setWindowTitle('一梦江湖-采集')
        window = QWindow.fromWinId(hwnd1)
        self.btn = QPushButton()
        self.btn.setText("开始采集")
        self.btn1 = QPushButton()
        self.btn1.setText('停止采集')
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

    def closeEvent(self, event):  # 函数名固定不可变
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        # QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply == QtWidgets.QMessageBox.Yes:
            os.remove('image/tpl1675244038936.png')
            os.remove('image/tpl1675244201268.png')
            os.remove('image/tpl1675395304672.png')
            os.remove('image/tpl1675396178938.png')
            os.system("taskkill /F /IM wyclx64.exe")
        else:
            event.ignore()  # 忽视点击X事件

    def get_title(hwnd):
        title = win32gui.GetWindowText(hwnd)
        return ('窗口标题:%s' % (title)) + '  ' + str(title)

    def caiji_start(self):
        self.thread1 = content_caiji()
        self.thread1.start()

    def caiji_stop(self):
        self.thread1.terminate()
        os.remove('image/tpl1675244038936.png')
        os.remove('image/tpl1675244201268.png')
        os.remove('image/tpl1675395304672.png')
        os.remove('image/tpl1675396178938.png')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())