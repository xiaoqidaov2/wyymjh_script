import win32api
import win32gui
import win32con
import os

def pc_clicked(hwnd, coordinate):
    tmp = win32api.MAKELONG(int(coordinate[0]), int(coordinate[1]))
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

def remove_images():
    for name in ['tpl1675244038936.png', 'tpl1675244201268.png', 'tpl1675395304672.png', 'tpl1675396178938.png']:
        try:
            os.remove(f'image/{name}')
        except FileNotFoundError:
            pass
