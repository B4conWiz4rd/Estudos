programa {
  funcao inicio() {
    real nota_prova
    real nota_trabalho
    real media_semestral
    logico atingiu_media_minima
    const real media_aprovacao = 7.0
    escreva("Digite a nota da prova: ")
    leia(nota_prova)
    escreva("Digite a nota do trabalho: ")
    leia(nota_trabalho)
    media_semestral = (nota_prova + nota_trabalho) / 2.0
    atingiu_media_minima = (media_semestral >= media_aprovacao)
    escreva("\n--- Relatório Semestral ---\n")
    escreva("Nota da Prova: ", nota_prova, "\n")
    escreva("Nota do Trabalho: ", nota_trabalho, "\n")
    escreva("Média Semestral: ", media_semestral, "\n")
    escreva("Você foi aprovado?: ", atingiu_media_minima)
  }
}