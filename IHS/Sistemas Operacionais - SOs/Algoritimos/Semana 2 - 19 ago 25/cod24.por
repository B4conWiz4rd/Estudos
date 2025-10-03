programa{
    funcao inicio(){
        real distancia, preco
        escreval("--- Calculadora de Preço de Passagem ---")
        escreva("Digite a distância a percorrer em Km: ")
        leia(distancia)
        se (distancia <= 200){
            preco = distancia * 0.50
            escreva("O preço da passagem é: ", preco,"R$" )
        }
        senao{
            preco = distancia * 0.45
            escreva("O preço da passagem é: ", preco,"R$" )
        }
    }
}