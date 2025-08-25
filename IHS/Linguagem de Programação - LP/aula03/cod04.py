#Decisão!
x = input('digite algo: ')
print ('É um número? ', x.isnumeric())
print ('É um alfanumérico? (números e letras)? ', x.isalnum())
print ('É um, alfabético (Letra) ', x.isalpha())
print ('Está em minpusculo?: ', x.islower())
print ('Está em maiúsculo? ', x.isupper())
print ('É somente espaço?', x.isspace())
print ('Está capitalizada (Possui maiúsculas e minusculas)', x.istitle())
