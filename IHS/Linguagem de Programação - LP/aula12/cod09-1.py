import pyautogui
import time


print("Iniciando a automação... Mova o mouse para o canto superior esquerdo da tela para cancelar.")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("notepad++")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(2)

pyautogui.hotkey("ctrl", "n")
time.sleep(1)
pyautogui.write("Festa Zumbiii")
pyautogui.hotkey("enter")
pyautogui.write("ÔOOoooUUUUUUUOOOooo")
pyautogui.hotkey("enter")
pyautogui.write("ja convidei a magrela e os carcas tbm")
pyautogui.hotkey("enter")
pyautogui.write("aq na Festa Zumbiii")
pyautogui.hotkey("enter")
time.sleep(1)

pyautogui.hotkey("ctrl", "s")
time.sleep(1.5)

pyautogui.write("anotacao.txt")
time.sleep(1)

time.sleep(1)
pyautogui.moveTo(x=489, y=111)
time.sleep(1)
pyautogui.leftClick(x=489, y=111)

caminho = r"C:\Users\Tec. Inf - Eddy\Desktop\Aooopa"
pyautogui.write(caminho)
time.sleep(1)

pyautogui.hotkey("enter")

time.sleep(1)
pyautogui.moveTo(x=783, y=556)
time.sleep(1)
pyautogui.leftClick(x=783, y=556)