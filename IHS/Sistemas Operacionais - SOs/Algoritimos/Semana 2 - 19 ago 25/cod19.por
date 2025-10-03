rograma {
    funcao inicio() {
        cadeia nome
        real nota1, nota2, media
        const real media_min =7.0
        logico aprovacao
        escreva("Digite o nome do aluno: ")
        leia(nome)
        escreva("Digite a primeira nota: ")
        leia(nota1)
        escreva("Digite a segunda nota: ")
        leia(nota2)
        media = (nota1 + nota2) / 2
        escreva("\n--- Boletim ---\n")
        escreva("Aluno: ",nome,"\n")
        escreva("Média: ", media,"\n")
        bom_aproveitamento = (media>=media_min)
        se (aprovacao) {
            escreva("Situação: APROVADO com bom aproveitamento!\n")
        } senao {
            escreva("Situação: REPROVADO, média abaixo de 7.0\n")
        }
    }
}