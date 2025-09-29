programa {
  funcao inicio() {
    inteiro n1, n2
    logico multiplo
    escreva("Digite o primeiro número inteiro: ")
    leia(n1)
    escreva("Digite o segundo número inteiro: ")
    leia(n2)
    multiplo = (n1 %n2 == 0)
    escreva("O primeiro é múltiplo do segundo? ", multiplo, "\n")
  }
}