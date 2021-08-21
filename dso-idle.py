import pyautogui
import pygetwindow
import time
import random
import os
import sys
import ctypes

random.seed(os.urandom(256))

dsoWindowTitle = "Drakensang Online | Das kostenlos spielbare Action-MMORPG - DSO"
try:
    dsoWindow = pygetwindow.getWindowsWithTitle(dsoWindowTitle)[0]
    dsoWindow.maximize()
    dsoWindow.activate()
except IndexError:
    ctypes.windll.user32.MessageBoxW(None, "DSO wurde nicht gestartet!", "Fehler", 0)
    sys.exit(0)

screenWidth, screenHeight = pyautogui.size()
halfOfScreenWidth = int(screenWidth / 2)
halfOfScreenHeight = int(screenHeight / 2)

while True:
    pyautogui.moveTo(
        halfOfScreenWidth - 100,
        screenHeight - halfOfScreenHeight - 30 # Window title bar
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))

    pyautogui.moveTo(
        halfOfScreenWidth + 93,
        screenHeight - halfOfScreenHeight - 30 # Window title bar
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))

    # ugh, hack, needed to determine if the window is still active. if it isn't, close the program gracefully
    try:
        pygetwindow.getWindowsWithTitle(dsoWindowTitle)[0]
    except IndexError:
        sys.exit(0)