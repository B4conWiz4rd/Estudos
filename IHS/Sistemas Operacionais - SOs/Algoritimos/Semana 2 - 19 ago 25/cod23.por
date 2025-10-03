programa {
    funcao inicio () {
        cadeia nome
        caracter genero
        real valor_total
        const real desconto_f = 0.13
        const real desconto_m = 0.05

        escreva ("Promoção dos dias das mulheres!\n")
        escreva ("Nome do(a) cliente: ")
        leia (nome)
        escreva ("Qual o seu gênero? [F/M]: ")
        leia (genero)
        escreva ("Qual o valor total da compra? ")
        leia (valor_total)
        se (genero == 'f') {
            escreva ("Parabens pelo seu dia! Mulheres recebem 13% de desconto hoje! \n")
            escreva ("--- Recibo ---\n")
            escreva ("Nome do cliente: ", nome, "\n")
            escreva ("Valor total: R$", valor_total, "\n")
            escreva ("Valor do desconto: R$", (desconto_f * valor_total), "\n")
            escreva ("TOTAL: ", valor_total-(desconto_m * valor_total))
        }


        senao {
            escreva ("Aqui homens tambem recebem desconto! 5% de desconto para presentear alguem especial! \n")
            escreva ("--- Recibo ---\n")
            escreva ("Nome do cliente: ", nome, "\n")
            escreva ("Valor total: R$", valor_total, "\n")
            escreva ("Valor do desconto: R$", (desconto_m * valor_total), "\n")
            escreva ("TOTAL: ", valor_total-(desconto_m * valor_total))
        }
    }
}