programa {
    funcao inicio() {
        inteiro n_cigarros, n_anos
        real w_time
        const inteiro min = 10
        const inteiro ano = 365
        const inteiro min_dia = 1440

        escreva ("Calculadora de redução de tempo de vida.\n")
        escreva ("Quantos cigarros você fuma por dia em média (ex: 2): ")
        leia (n_cigarros)
        escreva ("A quantos anos você fuma?(ex:2): ")
        leia (n_anos)
        w_time=((n_anos*ano*n_cigarros)*min)/min_dia
        escreva ("Você perderá aproximadamente ",w_time," dias de vida.")
    }
}