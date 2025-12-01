#funções servem para organizar o código, reutilizar e facilitar manutenção.

#   função simples

def saudacao():
    print("Bem-vindo")

#   chamando:

saudacao()

#   função com parâmetros

def soma (a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)
