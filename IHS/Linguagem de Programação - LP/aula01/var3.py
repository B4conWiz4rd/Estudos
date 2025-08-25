#Variáveis

##É utilizado input o usuário definir a varáivel como STRING##
nome = input ("Digite o seu nome: ")

print ("Olá",nome,"!")
##Para o código entender a variável definida pelo usuário como INTEIRO, é nescessário definila como INT##
idade = int(input ("Digite a sua idade: "))

print ("A idade do(a)",nome,"é de",idade,"anos!")

print ("Então no seu aniversário você fará",idade+1,"anos de idade!")

##Para o código entender a variável definida pelo usuário como REAL, é nescessário definila como FLOAT##
altura = float(input("Digite a sua altura: "))

print (f"Então,{nome} que tem, {idade} anos de idade, tem {altura:.2f} de altura? Caramba que incrível!!")