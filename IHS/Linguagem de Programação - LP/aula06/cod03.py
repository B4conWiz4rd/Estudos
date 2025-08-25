#DICIONÁRIO
pessoa = {
    'nome' : 'Edmilson',
    'idade' : 21,
    'peso' : '10 arrobas'
}
print (pessoa)
print (pessoa.keys())
print (pessoa.values())
pessoa ['altura'] = 'alguns'
print (f'O usuário {pessoa["nome"]} tem {pessoa["idade"]} anos de idade e pesa {pessoa["peso"]}, com {pessoa["altura"]} cm de altura. ')
pessoa ['peso'] = '11 arrobas'
print (f'O banco de dados foi atualizado, na verdade {pessoa["nome"]} pesa {pessoa["peso"]}.')
del pessoa ["idade"]
print ("nome" in pessoa)
print ("idade" in pessoa)