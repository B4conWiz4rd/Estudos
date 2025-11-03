import pyautogui
import time

# === CONFIGURAÇÃO DA TELA ===
# Resolução: 1920x1080 | Navegador 100%

pyautogui.alert(
    text='Iniciando a automação...',
    title='Automação de Login',
    button='OK'
)

pyautogui.alert(
    text='ATENTE-SE A ESTAR DELOGADO NO NAVEGADOR',
    title='ALERTA1',
    button='OK'
)

pyautogui.alert(
    text='ATENTE-SE QUE SEU MONITOR POSSUA A RESOLUÇÃO DE 1920x1080',
    title='ALERTA2',
    button='OK'
)

pyautogui.alert(
    text='ATENTE-SE QUE SEU NAVEGADOR POSSUA A RESOLUÇÃO DE 100%',
    title='ALERTA3',
    button='OK'
)

email = pyautogui.prompt(
    text='Digite o seu e-mail',
    title='Inserir E-mail'
)

senha = pyautogui.password(
    text='Digite a sua senha',
    title='Inserir Senha',
    mask='*'
)

navegador = pyautogui.confirm(
    text='Digite o seu navegador',
    title='Inserir Navegador',
    buttons=['Chrome', 'FireFox', 'Edge' , 'Opera']
)

resposta = pyautogui.confirm(
    text='Continuar a automação?',
    title='Confirmação',
    buttons=['Sim', 'Não']
)

if resposta == 'Sim':
    print("Iniciando navegador...")
    
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write(navegador)
    pyautogui.press('enter')
    time.sleep(4)

    pyautogui.write('https://www.google.com/')
    pyautogui.press('enter')
    time.sleep(3)

    time.sleep(1)
    pyautogui.moveTo(1682, 143, duration=1)
    pyautogui.click(x=1682, y=143)
    time.sleep(1)

    pyautogui.click(x=1065, y=509)
    time.sleep(0.5)
    pyautogui.write(email)

    pyautogui.click(x=1393, y=696)
    time.sleep(2)

    pyautogui.click(x=1050, y=540)
    time.sleep(0.5)
    pyautogui.write(senha)

    pyautogui.click(x=1019, y=560)
    time.sleep(1)
    pyautogui.click(x=1393, y=696)

    pyautogui.alert("Login concluído com sucesso!", "Sucesso")

elif resposta == 'Não':
    pyautogui.alert(
        text='Até a próxima!',
        title='Saindo',
        button='OK'
    )