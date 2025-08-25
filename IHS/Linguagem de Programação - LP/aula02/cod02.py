#Exemplo prático para usar mod (resto): Contágem de mese em um consorcio de bem
total_meses = int (input('Digite o total de meses: '))
ano = total_meses // 12
#Duas barras resultaram em uma simplificação
meses = total_meses % 12
print("O consorico é de ", ano, " anos e ", meses, " meses")