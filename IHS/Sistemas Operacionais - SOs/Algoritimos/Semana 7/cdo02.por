programa {
  funcao inicio() {
    inteiro n1, n2
    logico multiplo

    escreva("--- Verificado de Múltiplo ---\n")
    escreva("Digite o primeiro número inteiro: \n")
    leia (n1)
    escreva("Digite o sungundo número inteiro: \n")
    leia (n2)
    multiplo=(n1%n2==0)
    escreva("O primeiro é múltiplo do segundo? ",multiplo)
  }
}
