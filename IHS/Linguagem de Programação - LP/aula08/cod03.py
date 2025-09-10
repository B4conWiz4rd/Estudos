import cod01
print('Super conversor!')
print('1 - METRO -> CENTIMETRO')
print('2 - CENTIMETRO -> CENTIMETRO')
print('3 - KILOMETRO -> METRO')
opc=int(input('Selecione a opção desejada: '))
x=float(input('Digite o valor: '))

if opc == 1:{
    print('Resultado: ', cod01.mc(x))
}

elif opc == 2:{
    print('Resultado: ', cod01.cm(x))
}

elif opc == 3:{
    print('Resultado: ', cod01.km(x))
}

else: print('Opção inválida.')