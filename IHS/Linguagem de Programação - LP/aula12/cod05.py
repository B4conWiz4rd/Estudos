import pyautogui
import time

time.sleep(5)
pyautogui.moveTo(x=429, y=381)

pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)

pyautogui.moveTo(x=429, y=481)
pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)

pyautogui.moveTo(x=429, y=581)
pyautogui.dragRel(0,100, duration=2)
pyautogui.dragRel(100,0, duration=2)
pyautogui.dragRel(0,-100, duration=2)
pyautogui.dragRel(-100,0, duration=2)