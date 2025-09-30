n1 = str(input("Nome do primeiro aluno: "))
n2 = str(input("Nome do segundo aluno: "))
n3 = str(input("Nome do terceiro aluno: "))

with open ("alunos.txt","w") as arquivo:
    arquivo.write(f"{n1}")
    arquivo.write(f"\n{n2}")
    arquivo.write(f"\n{n3}")