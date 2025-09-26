programa {
  funcao inicio() {
    real nota_prova, nota_trabalho, media_semestral
    logico atingiu_media_minima
    const real media_aprovacao = 7.0

    escreva("-----Calculado de Média Semestral-----\n")
    escreva("Digite a nota da prova: \n")
    leia(nota_prova)
    escreva("Digite a nota do trabalho: \n")
    leia(nota_trabalho)
    media_semestral=nota_prova + nota_trabalho/ 2.0
    atingiu_media_minima=media_semestral>=media_aprovacao
    escreva("Nota da Prova: ", nota_prova,"\n")
    escreva("Nota do Trabalho: ", nota_trabalho, "\n")
    escreva("Média Semestral Calculada: ", media_semestral, "\n")
    escreva("Atingiu a média de aprovação: ", atingiu_media_minima)
  }
}
