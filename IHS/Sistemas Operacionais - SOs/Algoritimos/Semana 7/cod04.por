programa {
  funcao inicio() {
    logico condicao1 = verdadeiro
    logico condicao2 = falso
    logico condicao3 = verdadeiro
    logico resultado
    resultado = (condicao1 e condicao2) ou (nao condicao2 e condicao3)
    escreva("Resultado da expressão: ", resultado, "\n")
  }
}