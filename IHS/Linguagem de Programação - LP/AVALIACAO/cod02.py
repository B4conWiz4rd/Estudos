def log (nome):
    if nome == "Pedro":{print(f"Olá {nome}, bem vindo ao sistema!")}
    elif nome == "Edmilson": print(f"Olá {nome}, bem vindo ao sistema!")
    else: print("Olá Visitante, bem vindo ao sistema!")


nome=str(input("Informe seu usuário: "))
log(nome)