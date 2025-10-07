#No TERMINAL escreva " pip install pyautogui "
# pyautogui.moveto(1280,60,duration=2)
# pyautogui.moveto(280,300,duration=4)
# pyautogui.moveto(480,20,duration=7)
# pyautogui.moveto(37,1260,duration=3)

import pyautogui
import time
import random

# Obtém a largura e altura da tela
largura, altura = pyautogui.size()

while True:
    # Gera coordenadas X e Y aleatórias dentro dos limites da tela
    x_aleatorio = random.randint(0, largura)
    y_aleatorio = random.randint(0, altura)
    
    # Move o mouse para as coordenadas aleatórias
    # A duração de 1 segundo torna o movimento visível
    pyautogui.moveTo(x_aleatorio, y_aleatorio, duration=1)
    
    # Imprime a nova posição do mouse no terminal
    print(pyautogui.position())
    
    # Espera 2 segundos antes de mover novamente
    time.sleep(2)