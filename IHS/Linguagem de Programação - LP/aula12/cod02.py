import pyautogui
import time
import random

i = int(1)
#resolução do monitor
vertical, horizontal = pyautogui.size()

while (i <= 3):

    x_aleatorio = random.randint(0, horizontal)
    y_aleatorio = random.randint(0, vertical)
    
    pyautogui.moveTo(x_aleatorio, y_aleatorio, duration=1)

    time.sleep(2)
    
    i = (i+1)
