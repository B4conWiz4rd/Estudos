programa {
  funcao inicio() {
    inteiro i,quantidade[3]
    cadeia item[3]
    real valor[3],total[3]

    i = 1
    escreva ("--- Supermercado Preço Bom ---\n")
    enquanto (i<=2) {
    escreva ("--- Produto ",i," ---\n")
    escreva ("Digite o nome do produto: ")
    leia (item[i])
    escreva ("Digite quantidade: ")
    leia (quantidade[i])
    escreva ("Digite o preço unitário (ex: 8.99) ")
    leia (valor[i])
    i= i+1
    }
    i = 1
    escreva ("--- RECIBO DA COMPRA ---\n")
    enquanto (i<=2){
    escreva ("Item ",item[i],"\n")
    escreva ("Qtde: ", quantidade[i]," | Preço Unit: ",valor[i])
    escreva (" | Subtotal ",quantidade[i]*valor[i],"\n")
    total[i] = quantidade[i]+valor[i]
    i= i+1
    }
    escreva ("-------------------------------------\n")
    escreva ("VALOR TOTAL DA COMPRA: ", total[1]+total[2],"\n")
    escreva ("-------------------------------------\n")
  }
}
