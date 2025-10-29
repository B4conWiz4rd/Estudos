import pyautogui
import time

pyautogui.alert(
    text='iniciando a automação.',
    title='atomação de login',
    button='ok'
    )

email = pyautogui.prompt(
    text='digite o seu e-mail',
    title='informações obrigatórias'
    )

print(f'Seu email: {email}')

resposta = pyautogui.confirm(
    text='continuar a nossa automação?',
    title='confimação',
    buttons=['sim','não','cancelar']
    )

print(resposta)