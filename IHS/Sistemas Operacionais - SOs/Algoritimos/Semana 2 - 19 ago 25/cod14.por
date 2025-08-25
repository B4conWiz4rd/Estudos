programa {
  funcao inicio() {
    real n1, n2
    escreva ("Calculadora de preço, locação de carros.\n")
    escreva ("Olá usuário, digite o total de dias com o carro em posse: ")
    leia (n1)
    escreva ("Digite o total de km percorridos: ")
    leia (n2)
    escreva ("O total a pagar é: R$ ",(n1*90)+(n2*0.20))
  }
}
