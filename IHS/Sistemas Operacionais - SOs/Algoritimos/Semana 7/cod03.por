programa {
  funcao inicio() {
    real p1, p2
    logico preco
    escreva("Digite o preço do Produto A: ")
    leia(p1)
    escreva("Digite o preço do Produto B: ")
    leia(p2)
    escreva("\nPreço do Produto A: ", p1, "\n")
    escreva("Preço do Produto B: ", p2, "\n")
    preco = (p1<p2)
    escreva("Produto A é mais barato que B? ", preco, "\n")
    preco = (p1 == p2)
    escreva("Os preços são iguais? ", preco, "\n")
  }
}