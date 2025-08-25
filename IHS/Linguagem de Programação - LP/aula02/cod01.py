#Escreva um programa que receba 2 valores inteiro x e y e calcule o valor de z: Z=y^2+y^2/(x-y)^2

x = int (input('Digite o valor para x: '))
print (x)

y = int (input('Digite o valor para y: '))
print (y)

z = (x**2 + y**2) / (x - y)**2
print ('z: ', z)

