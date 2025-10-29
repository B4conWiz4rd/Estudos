import pyautogui
import time

pyautogui.press ("win")
time.sleep (1)
pyautogui.write ("firefox")
time.sleep (1)
pyautogui.press ("enter")
time.sleep (3)
pyautogui.write ("https://www.youtube.com/")
time.sleep (2)
pyautogui.press ("enter")
time.sleep (2)
pyautogui.moveTo (x=701, y=144)
pyautogui.leftClick (x=701, y=144)
time.sleep (1)
pyautogui.write ("festa zumbi")
time.sleep (1)
pyautogui.press ("enter")