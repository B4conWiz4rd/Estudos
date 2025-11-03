import pyautogui
import time

# Mensagem inicial
pyautogui.alert(
    text='Iniciando a automação.',
    title='Automação de Login',
    button='OK'
)

# Pergunta o username
user_name = pyautogui.prompt(
    text='Digite o seu username',
    title='Informações Obrigatórias'
)

# Confirmação
resposta = pyautogui.confirm(
    text='Continuar a automação?',
    title='Confirmação',
    buttons=['Sim', 'Não']
)

if resposta == 'Sim':
    pyautogui.alert(
        text='Diga Xis :D',
        title='Começando',
        button='Xiiiis'
    )
    time.sleep(3)

    # Abre o Executar (Win + R)
    pyautogui.hotkey('win', 'r')
    time.sleep(1)

    # Digita o caminho da imagem e pressiona Enter
    caminho_imagem = r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula14\cod02\images.jpg'
    time.sleep(1)
    pyautogui.write(caminho_imagem)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)  # Espera a imagem abrir

    # Captura a tela e salva
    img1 = pyautogui.screenshot()
    img1.save('image4.png')

    pyautogui.alert(
        text='Imagem capturada e salva como image4.png!',
        title='Sucesso',
        button='OK'
    )

elif resposta == 'Não':
    pyautogui.alert(
        text='Até a próxima!',
        title='Terminado',
        button='Xiiiis'
    )