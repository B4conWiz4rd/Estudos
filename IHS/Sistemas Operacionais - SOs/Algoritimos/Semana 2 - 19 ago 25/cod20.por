programa{
    funcao inicio (){
        inteiro num
        logico validacao
        escreva ("Escreva um número inteiro: ")
        leia (num)

        validacao = num%2==0
        se (validacao) {
            escreva ("Seu número é par")
        }
        senao {
            escreva ("Seu número é impar")
        }
    }
}