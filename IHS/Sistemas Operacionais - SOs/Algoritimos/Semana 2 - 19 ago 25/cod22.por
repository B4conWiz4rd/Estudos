programa {
    funcao inicio (){
        caracter genero
        inteiro idade
        const inteiro idade_min = 18
        logico validacao
        escreva ("Qual é se gênero? [F/M]")
        leia (genero)
        se (genero=="m"){
            escreva ("Qual a sua idade?")
            leia (idade)
            validacao = idade_min <= idade

                se (validacao){
                    escreva("Você é obrigado a se apresentar ao departamento mais próximo")
                }

                senao {
                    escreva("Não é necessário apresentar-se ao quartel, já que não atingiu a iodade minima.")
                }
        }

        senao {
            escreva("Não é necessário alistação obrigatória, caso queira alistar-se procure o departamento mais próximo.")
        }
    }
}