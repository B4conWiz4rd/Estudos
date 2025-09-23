#Trabalho
#Peça ao usuário um número e tente converter para o tipo inteiro.
#Caso o usuário digite um valor inválido, exiba uma mensagem de erro.
try:
    n = int(input("Digite um número inteiro válido"))
except ValueError:
    print("Erro: Número inválido. Por Favor, digite um número inteiro.")
else:
    print(f"Seu número é válido")
finally:
    print("Fim do programa")