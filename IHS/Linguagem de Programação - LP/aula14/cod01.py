import pyautogui
import time

#resolução 1920x1080
#proporção do navegador = 100%

pyautogui.alert(
    text='iniciando a automação.',
    title='atomação de login',
    button='ok'
    )

email = pyautogui.prompt(
    text='digite o seu e-mail',
    title='insirir_email'
    )

senha = pyautogui.prompt(
    text='digite a sua senha',
    title='insirir_senha'
    )

resposta = pyautogui.confirm(
    text='continuar a nossa automação?',
    title='confimação',
    buttons=['sim','não']
    )

if (resposta == 'sim') : 
    pyautogui.press ('win')
    time.sleep(3)
    pyautogui.write('firefox')
    time.sleep(2)
    pyautogui.press ('enter')
    time.sleep (2)
    pyautogui.write ('https://www.google.com/')
    time.sleep(2)
    pyautogui.press ('enter')
    
    time.sleep(1)
    pyautogui.moveTo(1682, 143, duration=1)
    pyautogui.click(x=1682, y=143)

    time.sleep(1)
    pyautogui.moveTo(1065, 509, duration=1)
    pyautogui.click(x=1065, y=509)
    pyautogui.write(email)

    pyautogui.moveTo(1393, 696, duration=1)
    pyautogui.click(x=1393,y=696)

    time.sleep(1)
    pyautogui.moveTo(1050, 540, duration=1)
    pyautogui.click(x=1050, y=540)
    pyautogui.write(senha)
    pyautogui.moveTo(1019, 560, duration=1)
    pyautogui.click(x=1019, y=560)
    time.sleep(1)
    pyautogui.moveTo(1393, 696, duration=1)

if resposta == 'não' : 
    pyautogui.alert(
    text='Até a próxima!',
    title='exit',
    button='ok'
    )