import os
import base64
import random
import time
from airtest.core.api import *
from image_resources import img1, img2, img3, img4
from utils import pc_clicked
import win32gui
from PyQt5.QtCore import QThread

class ContentCaiji(QThread):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.hwnd = win32gui.FindWindow(None, '一梦江湖-采集')
        if self.hwnd:
            self.hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd, lambda hwnd, param: param.append(hwnd), self.hwndChildList)
            self.hwnd1 = win32gui.FindWindowEx(self.hwndChildList[0], 0, None, None)
            auto_setup(__file__, devices=["Windows:///" + str(self.hwnd1)])

    def run(self, r=100, w=0):
        self.setup_images()
        b = 0
        while b < r:
            if exists(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105), resolution=(1175, 789))):
                print('开始采集')
                pc_clicked(self.hwnd1, exists(Template(r"image/tpl1675244201268.png", record_pos=(0.344, 0.105), resolution=(1162, 789))))
                while exists(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105), resolution=(1175, 789))):
                    print('正在检测采集进度')
                    time.sleep(0.5)
            else:
                self.handle_wait(w)
                w = (w + 1) % 4

    def setup_images(self):
        os.makedirs("image", exist_ok=True)
        for img, name in zip([img1, img2, img3, img4], ['tpl1675244038936.png', 'tpl1675244201268.png', 'tpl1675395304672.png', 'tpl1675396178938.png']):
            with open(f'image/{name}', 'wb') as f:
                f.write(base64.b64decode(img))

    def handle_wait(self, w):
        wait(Template(r"image/tpl1675395304672.png", threshold=0.8, record_pos=(0.383, -0.232), resolution=(1170, 638)))
        tmp = exists(Template(r"image/tpl1675395304672.png", threshold=0.8, record_pos=(0.383, -0.232), resolution=(1170, 638)))
        pc_clicked(self.hwnd1, tmp)
        if w != 3:
            d = random.randint(1, 5 - w)
            huanxian = exists(Template(r"image/tpl1675396178938.png", record_pos=(0.275, -0.215), resolution=(1170, 638)))
            tmp = [int(huanxian[0]), int(round(huanxian[1] * d))]
            pc_clicked(self.hwnd1, tmp)
            wait(Template(r"image/tpl1675244038936.png", record_pos=(0.337, 0.105), resolution=(1175, 789)))
            time.sleep(1)
