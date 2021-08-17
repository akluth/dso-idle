import pyautogui
import pygetwindow
import time
import random
import os

random.seed(os.urandom(256))

dsoWindow = pygetwindow.getWindowsWithTitle("Drakensang Online | Das kostenlos spielbare Action-MMORPG - DSO")[0]
dsoWindow.maximize()
dsoWindow.activate()

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

thirdOfScreenWidth = screenWidth / 3

while True:
    pyautogui.moveTo(
        screenWidth - (thirdOfScreenWidth),
        screenHeight - (screenHeight / 2)
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))

    pyautogui.moveTo(
        screenWidth - (thirdOfScreenWidth * 2),
        screenHeight - (screenHeight / 2)
    )
    pyautogui.click()
    time.sleep(random.randint(1, 60))
