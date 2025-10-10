import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad++")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "n")
time.sleep(1)
pyautogui.write("Automatizar com PyAutoGUI é divertido!")
