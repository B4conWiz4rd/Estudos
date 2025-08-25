#CONSIDERE UM DICIONÁRIO COM 5 NOMES DE ALUNOS E SUAS NOTAS
#ESCREVA UM PROGRAMA QUE CALCULER A MÉDIA DESSES ALUNOS
a = {
    'Jubliqueuda': 4.70,
    'Baphomet': 7.0,
    'Fulano': 8.7,
    'Ciclano': 7.2,
    'Breutano': 10
}
m = sum(a.values())/5
print (f'A média das notas são de {m}.')