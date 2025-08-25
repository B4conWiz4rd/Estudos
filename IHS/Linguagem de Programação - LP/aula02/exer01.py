#Exercicio! Um programa que vai ler duas notas de um aluno, vai calcular a média, para ser aprovado a média terá que ser maior que 60%
prova = float (input ('Qual é o total da prova?: '))
prova = prova / 0.6
nota = float (input ('Digite a nota do aluno: '))
if nota >= prova: print ('YAY! A cima da média, ai sim!')
else : print ('PUTZ! A baixo da média, continue firme e prepare-se para a próxima! ')