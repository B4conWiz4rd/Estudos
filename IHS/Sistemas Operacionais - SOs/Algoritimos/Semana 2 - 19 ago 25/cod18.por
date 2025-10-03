programa {
    funcao inicio () {
        const inteiro idade_min = 16
        inteiro idade

        escreva ("Você já pode votar?\n")
        escreva ("Qual a sua idade?: ")

        leia (idade)

        se (idade > idade_min) {
            escreva("Com",idade," anos, você já pode votar!")
        }

        senao {
            escreva("Você ainda não pode votar, a idade minima é ",idade_min," anos!")
        }
    }