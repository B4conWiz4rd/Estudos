import pyautogui
import time

#pausa de 0.3 segundos a cada comando
pyautogui.press ("win")
time.sleep (1)
pyautogui.write ("notepad++")
time.sleep (1)
pyautogui.press ("enter")
time.sleep (1)
pyautogui.write ("edzada")
time.sleep (1)
pyautogui.hotkey ("alt","f4")