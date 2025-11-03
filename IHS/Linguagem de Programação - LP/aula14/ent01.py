import pyautogui
import time
import os
import win32gui
import win32con

# === CONFIGURAÇÕES ===
caminho = r'C:\Users\Tec. Inf - Eddy\Downloads\Pokemon - FireRed Version (USA, Europe) (Rev 1).gba'

# Nome exato da janela do mGBA (você confirmou!)
janela_alvo = "mGBA - Pokemon - FireRed Version"

# Quantos X pra pular intro (FireRed = 11)
quantos_x = 11

# Delay entre X (com Fast Forward = MUITO rápido)
delay_x = 0.15  # ~1.5 segundos no total!

# =====================

if not os.path.exists(caminho):
    print(f"Erro: ROM não encontrada!\n{caminho}")
    exit()

print("Abrindo Pokémon FireRed no mGBA...")

# 1. Abre via Win + R
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write(f'"{caminho}"')
pyautogui.press('enter')
time.sleep(6)  # Espera carregar

# 2. Força foco na janela do mGBA
def ativar_janela(titulo_parcial):
    def callback(hwnd, windows):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowVisible(hwnd) and titulo_parcial in title:
            windows.append((hwnd, title))
        return True
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    if windows:
        hwnd, title = windows[0]
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        print(f"✅ Janela ativada: {title}")
        time.sleep(0.8)
        return True
    return False

if not ativar_janela(janela_alvo):
    print("❌ ERRO: Janela do mGBA não encontrada. Abra manualmente e tente de novo.")
    exit()

print("⚡ Ativando Fast Forward...")
pyautogui.hotkey('shift', 'tab')
time.sleep(5)

print("Pressionando Start...")
pyautogui.press('return')
time.sleep(1.8)
pyautogui.press('return')
time.sleep(1.8)

print(f"⏩ Pulando intro com {quantos_x} X's...")
for i in range(quantos_x):
    pyautogui.press('x')
    time.sleep(delay_x)

print("\n🎉 PRONTO! Intro pulada em alta velocidade!")
print("   Bora caçar Pokémon, treinador! 🚀")