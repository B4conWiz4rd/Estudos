import pyautogui
import time

time.sleep(5)

try:
    while True:
        posicao=pyautogui.position()
        print(f"X: {posicao.x:<4} Y: {posicao.y:<4}", end='\r')

except:
    print("Fim do programa")