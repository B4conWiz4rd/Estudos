#usamos várias vezes para tarefas de automação

import pyautogui

pyautogui.moveTo (600, 500, duration=2)

#   clicar

pyautogui.click()

#   digitar

pyautogui.write("Olá mundo!", interval=0.1)

#   pressinar tela

pyautogui.press("enter")

#   exemplos de automação

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("Olá, este texto foi digitado automaticamente!", interval=0.07)