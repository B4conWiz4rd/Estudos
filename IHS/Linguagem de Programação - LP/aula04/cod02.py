#Descobrir o Maior de Dois Números
#Peça ao usuário para digitar dois npumeros inteiros e mostre qual deles é maior. Caso sejam iguais informe que são iguais.
n1 = int(input('Digite o priemiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 == n2: print ('Erro! Os números são iguais')
elif n1 > n2 : print('O número ',n1,' é maior que ', n2,'.')
else: print('O número ', n2,' é maior que ', n1,'.')