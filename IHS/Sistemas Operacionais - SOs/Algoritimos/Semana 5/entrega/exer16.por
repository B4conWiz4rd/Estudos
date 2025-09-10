programa {
  funcao inicio() {
    const cadeia magia = ("Exura Sio")
    const inteiro mpw = 140
    inteiro num

    escreva ("--- Calculadora de Custo de Mana (Magia:",magia,") ---\n")
    escreva ("Quantas vezes você pretende lançar a magia ",magia,"? : ")
    leia (num)
    escreva("\nPara lançar a magia '", magia, "' ", num, " vez(es), você gastará: ", (num*mpw), " de mana.\n")
  }
}
