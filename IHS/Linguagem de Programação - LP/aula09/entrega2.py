#Crie um programa que pergunta ao usuário seu nome e idade e grave em um arquivo txt
nome = str(input("Qual o seu nome? "))
idade = str(input("Qual a sua idade? "))

with open ("datab.txt","w") as arquivo:
    arquivo.write(nome)
    arquivo.write(f"\n{idade}")