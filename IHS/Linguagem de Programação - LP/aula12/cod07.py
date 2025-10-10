import pyautogui
import time

pyautogui.press ("win")
time.sleep (1)
pyautogui.write ("firefox")
time.sleep (1)
pyautogui.press ("enter")
time.sleep (3)
pyautogui.write ("https://www.wikipedia.org/")
time.sleep (2)
pyautogui.press ("enter")