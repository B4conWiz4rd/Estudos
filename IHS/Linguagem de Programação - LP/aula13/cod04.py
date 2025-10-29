import pyautogui
import time

print("O script começará em 5 segundos. Prepare-se...")
time.sleep(5)

print("Agora, passe o mouse sobre o canto superior esquerdo da janela.")
time.sleep(5)
p_inicial = pyautogui.position()
print(f"Canto superior esquerdo guardado: {p_inicial}")

time.sleep(2) # Uma pequena pausa para o usuário se mover
print("Agora, passe o mouse sobre o canto inferior direito da janela.")
time.sleep(5)
p_final = pyautogui.position()
print(f"Canto inferior direito guardado: {p_final}")

# --- LINHAS CORRIGIDAS ---
largura = p_final.x - p_inicial.x
altura = p_final.y - p_inicial.y
# -------------------------

print("\n--- Resultado ---")
print(f"Área da janela:")
print(f"  - Posição inicial (x, y): {p_inicial.x}, {p_inicial.y}")
print(f"  - Largura: {largura}")
print(f"  - Altura: {altura}")
print(f"------------------")
print(f"Parâmetros para usar em pyautogui.locateOnScreen ou pyautogui.screenshot:")
print(f"region=({p_inicial.x}, {p_inicial.y}, {largura}, {altura})")