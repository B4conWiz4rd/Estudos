programa {
  funcao inicio() {
    cadeia item
    real peso
    inteiro qtd

    escreva ("Nome do item: ")
    leia (item)
    escreva ("Peso uniário: ")
    leia (peso)
    escreva ("Quantidade em posse: ")
    leia (qtd)
    escreva ("--- Detalhe da Bag ---")
    escreva ("Item: ", item,"\n")
    escreva ("Quantidade: ", peso,"\n")
    escreva ("Peso unitário: ", qtd,"\n")
    escreva ("Peso Total: ", peso*qtd,"\n")
  }
}
