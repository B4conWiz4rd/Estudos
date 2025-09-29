programa {
  funcao inicio() {
    const real percentual_desconto = 0.10
    cadeia nome_cliente, forma_pagamento
    real valor_total, valor_desconto, valor_final
    logico ganhou_brinde
    escreva("--- Sistema de Caixa da Loja ---\n")
    escreva("Nome do Cliente: ")
    leia(nome_cliente)
    escreva("Valor total dos produtos: R$ ")
    leia(valor_total)
    escreva("Forma de pagamento (PIX ou Cartão): ")
    leia(forma_pagamento)
    valor_desconto = valor_total * percentual_desconto
    valor_final = valor_total - valor_desconto
    ganhou_brinde = (valor_final > 100.0 e forma_pagamento == "PIX")
    escreva("\n--- Recibo para ", nome_cliente, " ---\n")
    escreva("Valor dos Produtos: R$ ", valor_total , "\n")
    escreva("Desconto (10%): R$ ", valor_desconto, "\n")
    escreva("Valor Final da Compra: R$ ", valor_final, "\n")
    escreva("Forma de Pagamento: ", forma_pagamento, "\n")
    escreva("Cliente ganhou brinde especial? ", ganhou_brinde, "\n")
  }
}