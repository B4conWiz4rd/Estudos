#Manipulação de arquivo
#r-read (leia)
#w-write (escreva-subscreve)
#a-append (???)
with open ("dados.txt","w") as arquivo:
    arquivo.write("Edzada")


with open ("dados.txt","r") as arquivo:
    dados.txt=arquivo()
    print(conteudo)

with open("dados.txt","a") as arquivo:
    arquivo.write("\n o Cara!")