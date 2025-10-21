import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("mspaint")
time.sleep(1)
pyautogui.hotkey("enter")

time.sleep(5)
pyautogui.moveTo(x=429, y=381)

pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)

pyautogui.moveTo(x=629, y=381)
pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)

pyautogui.moveTo(x=829, y=381)
pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)