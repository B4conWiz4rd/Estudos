#,acro para ir no link "gmail" dento da página "google.com" funciona somente no cumputador da escola devido a resolução.

import pyautogui
import time
import random

email= "edmilson.castro.filho@gmail.com"
senha= "definitivamente uma senha :)"

time.sleep(3)
pyautogui.moveTo(1682, 143, duration=2)
pyautogui.click(x=1682, y=143)

time.sleep(2)
pyautogui.moveTo(1065, 509, duration=2)
pyautogui.click(x=1065, y=509)
pyautogui.write(email)

pyautogui.moveTo(1393, 696, duration=2)
pyautogui.click(x=1393,y=696)

time.sleep(2)
pyautogui.moveTo(1530, 288, duration=2)
pyautogui.click(x=1530, y=288)
pyautogui.moveTo(995, 606, duration=2)
pyautogui.click(x=995, y=606)
pyautogui.moveTo(1019, 560, duration=2)
pyautogui.click(x=1019, y=560)
pyautogui.write(senha)
time.sleep(4)
pyautogui.moveTo(1393, 696, duration=2)
