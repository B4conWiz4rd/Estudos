programa {
    funcao inicio () {
        inteiro vel_carro
        const inteiro vel_max = 80

        escreva("Qual a velocidade do carro registrada? ")
        leia (vel_carro)

        se (vel_carro > vel_max) {
            escreva("O carro está a cima da velocidade permitida! \n")
            escreva("Você foi multado em: ",(vel_carro-vel_max)*5,"R$.")            
        }

        senao {
            escreva ("O carro está circulando na velocidade permitida. ")
        }
    }
}