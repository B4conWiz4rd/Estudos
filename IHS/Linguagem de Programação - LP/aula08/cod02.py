import cod01

print('Super Calculadora!')
print('1 - ADIÇÃO')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPLICAÇÃO')
print('4 - DIVISÃO')

fator=int(input('Com qual operação deseja seguir a conta?: '))
x=float(input('Insira o primeiro número: '))
y=float(input('Insira o segundo número: '))

if fator == 1:{
    print('Resultado: ', cod01.soma(x,y))
}

elif fator == 2:{
   print('Resultado: ', cod01.subt(x,y)) 
}

elif fator == 3:{
    print('Resultado: ', cod01.mul(x,y))
}
    
elif fator == 4:{
    print('Resultado: ', cod01.div(x,y))
}

else:
    print ('opção inválida')