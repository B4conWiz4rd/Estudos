programa{
    funcao inicio (){
        inteiro num
        logico validacao
        escreva ("Digite o anos referente em ano que deseja (caso '1984' digite '84'): ")
        leia (num)

        validacao = num%4 == 0
        se (validacao) {
            escreva ("Seu ano é bisexto")
        }
        senao {
            escreva ("Seu ano não é bisexto")
        }
    }
}