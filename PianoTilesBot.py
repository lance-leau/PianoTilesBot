# https://www.agame.com/game/magic-piano-tiles

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# 1st column x:520
# 2nd column x:620
# 3rd column x:720
# 4th comumn x:820

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(520, 700) [0] == 0:
        click(520, 700)
    if pyautogui.pixel(620, 700) [0] == 0:
        click(620, 700)
    if pyautogui.pixel(720, 700) [0] == 0:
        click(720, 700)
    if pyautogui.pixel(820, 700) [0] == 0:
        click(820, 700)
