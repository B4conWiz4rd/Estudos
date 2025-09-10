programa {
  funcao inicio() {
    const inteiro xp_mob1 = 400
    const real gp_mob1 = 57
    const real oz_mob1 = 0.97
    const cadeia nam_mob1 = "Adept of the Cult"

    const inteiro xp_mob2 = 750
    const real gp_mob2 = 105
    const real oz_mob2 = 1.28
    const cadeia nam_mob2 = "Mutated Tiger"

    const inteiro xp_mob3 = 25
    const real gp_mob3 = 5
    const real oz_mob3 = 9.1
    const cadeia nam_mob3 = "Swamp Troll"

    const inteiro xp_mob4 = 150
    const real gp_mob4 = 25.5
    const real oz_mob4 = 3.2
    const cadeia nam_mob4 = "Cyclops"

    cadeia mob, char
    real hunt_time, repot_price
    inteiro mob_hunt

    escreva ("--- Relatório Detalhado de Caça no Tibia ----\n")
    escreva ("Monstro Caçado: ")
    leia (mob)

    se (mob == nam_mob1) {
      escreva ("Nome do seu Personagem: ")
      leia (char)
      escreva ("Quantos ",nam_mob1,"(s) você derrotou? ")
      leia (mob_hunt)
      escreva ("Tempo total de caçada (em horas, exemplo: 1.5 para 1h 30): ")
      leia (hunt_time)
      escreva ("Custo total de suprimentos (poções, etc) em GPs: ")
      leia (repot_price)
      escreva ("\n")
      escreva ("--- Relatório da Caçada de ",char," ---\n")
      escreva ("Monstro Focado: ", nam_mob1,"\n")
      escreva ("Quantidade Derrotada: ",mob_hunt,"\n")
      escreva ("Tempo da Hunt: ",hunt_time,"\n")
      escreva ("-------------------------------------------\n")
      escreva ("XP Total Ganho: ",(xp_mob1*mob_hunt))
      escreva ("GP Total Ganho: ", (gp_mob1*mob_hunt))
      escreva ("Peso estimado Loot: ",(oz_mob1*mob_hunt))
    }
  }
}
