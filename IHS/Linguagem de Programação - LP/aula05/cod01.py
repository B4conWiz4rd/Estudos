#Lista | Conjunto sequencial de valores - ÍNDICE
#nome_lista = [valor1,valor2,valor3]
#pisicoes_lista = [0,1,2,3,4,5,6,7,8,9,10,...]
numero = [2,5,10,1,4,9,22,100,3]
print (len(numero)) #len - mostra o dos itens na lista
print (min(numero)) #min - mostra o menor valor da lista
print (max(numero)) #max - mostra o maior valor da lista
print (sum(numero)) #sum - mostra a soma de todos o valores da lista
print (sorted(numero)) #sort - mostra os valores organizados do maior para o menor
print (sorted(numero, reverse=True)) #reverse= - aplicando-o após a variável, mostra os valores do menor para o maior
print (numero[1]) #[] - Mostra o número na posição 1, lembrando que o a lista começa com 0
print (100 in numero) #in - é uma condição, mostra se um número está presente a lista
print (numero) #mostra a variável, nesse caso os valores dentro da lista
print (numero [2:8]) #mostra a variável, aplicar [] após a varável possibilita mostrar os valores referentes ao número da lista, lembrando que a lista começa com 0
numero.append (101) #Determina a adição de valor ao final da lista, determinando-o irá adicionar uma nova posição a lista
print (numero)
del numero [1] #Determina a exclusão do valor referente a posição da lista, apartir dela, o valor será excluido
print (numero)