import pyautogui
import pygetwindow
import time
import random
import os
import sys

random.seed(os.urandom(256))

dsoWindowTitle = "Drakensang Online | Das kostenlos spielbare Action-MMORPG - DSO"
dsoWindow = pygetwindow.getWindowsWithTitle(dsoWindowTitle)[0]
dsoWindow.maximize()
dsoWindow.activate()

screenWidth, screenHeight = pyautogui.size()
thirdOfScreenWidth = int(screenWidth / 3)
halfOfScreenHeight = int(screenHeight / 2)

while True:
    pyautogui.moveTo(
        screenWidth - thirdOfScreenWidth,
        screenHeight - halfOfScreenHeight
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))

    pyautogui.moveTo(
        screenWidth - thirdOfScreenWidth * 2,
        screenHeight - halfOfScreenHeight
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))

    # ugh, hack, needed to determine if the window is still active. if it isn't, close the program gracefully
    try:
        pygetwindow.getWindowsWithTitle(dsoWindowTitle)[0]
    except IndexError:
        sys.exit(0)