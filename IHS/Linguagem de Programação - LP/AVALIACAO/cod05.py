try:
    print('Super calculadora de divisão')
    n1=float(input("Informe seu primeiro número: "))
    n2=float(input("Informe seu segundo número: "))
    print (f"O resultado de {n1} dividido por {n2} é igual a {n1/n2}")

except ZeroDivisionError:
    print("Erro! Número divisivel por Zero")