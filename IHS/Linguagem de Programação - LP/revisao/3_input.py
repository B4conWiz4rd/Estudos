#Usado para receber dados do usuário

nome = input("Digitete seu nome: ")
idade = int(input("Digite a sua idade: "))

print(f"olá, {nome}. Você tem {idade} anos.")

#IMPORTANTE: tudo que vem do input é str.
#para numeros, convertem: int(), float()