#ESCREVA UM PROGRAMA QUE PERGUNTE A QAUNTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
#CALCULE O PREÇO A PAGAR, SABENDO QUE P CARRO CUSTA R$60.00 POR DIA E R$0.15 POR KM
print('Olá usuário, para calcular o valor a pagar precisamos saber:')
n1 = int (input('Total de dias com o carro em posse: '))
n2 = float (input('Total de KM rodados: '))
n3 = float ((n1*60)+(n2*0.15))
print (f"A quantidade de dias com o carro em posse foi {n1}, foram rodados {n2}KM, totalizando R${n3} a pagar.")