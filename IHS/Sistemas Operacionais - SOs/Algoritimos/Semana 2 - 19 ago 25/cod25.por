programa {
    funcao inicio () {
        real reta_a, reta_b, reta_c
        logico triangulo

        escreva("Digite o valor da primeira reta: ")
        leia (reta_a)
        escreva("Digite o valor da segunda reta: ")
        leia (reta_b)
        escreva("Digite o valor da terceira reta: ")
        leia (reta_c)

        triangulo = (reta_a<reta_b+reta_c) e (reta_b< reta_a +reta_c) e (reta_c<reta_a+reta_b)

        se (triangulo){
        escreva ("é um triangulo!")
        }
        senao {
        escreva ("não é triangulo")
        }
    }
}