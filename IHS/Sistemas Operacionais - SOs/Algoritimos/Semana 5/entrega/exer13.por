programa {
  funcao inicio() {
    real pgas, cons, dist

    escreva ("Preço do combustível (R$/L): ")
    leia (pgas)
    escreva ("Consumo do carro (Km/L): ")
    leia (cons)
    escreva ("Distância da viagem (Km): ")
    leia (dist)
    escreva ("O custo da viágem será de R$ ",(pgas/cons)*dist)
  }
}
