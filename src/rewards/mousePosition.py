import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print("Mouse position: ({}, {})".format(x, y))
    time.sleep(1)