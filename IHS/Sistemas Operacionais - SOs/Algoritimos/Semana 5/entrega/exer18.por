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
      escreva ("XP Total Ganho: ",(xp_mob1*mob_hunt),"\n")
      escreva ("GP Total Ganho: ", (gp_mob1*mob_hunt),"\n")
      escreva ("Peso estimado Loot: ",(oz_mob1*mob_hunt)," Oz\n")
      escreva ("-------------------------------------------\n")
      escreva ("Custo dos Suprimentos: ",(repot_price),"\n")
      escreva ("Lucro/Prejuiso Estimado: ",((gp_mob1*mob_hunt)-repot_price),"\n")
      escreva ("-------------------------------------------\n")
      escreva ("Média de XP por Hora: ",((xp_mob1*mob_hunt)/hunt_time),"\n")
      escreva ("Média de GP por Hora: ",((gp_mob1*mob_hunt)/hunt_time),"\n")
       escreva ("-------------------------------------------\n")
      escreva ("Bom jogo, ",char,"\n")
    }

    se (mob == nam_mob2) {
      escreva ("Nome do seu Personagem: ")
      leia (char)
      escreva ("Quantos ",nam_mob2,"(s) você derrotou? ")
      leia (mob_hunt)
      escreva ("Tempo total de caçada (em horas, exemplo: 1.5 para 1h 30): ")
      leia (hunt_time)
      escreva ("Custo total de suprimentos (poções, etc) em GPs: ")
      leia (repot_price)
      escreva ("\n")
      escreva ("--- Relatório da Caçada de ",char," ---\n")
      escreva ("Monstro Focado: ", nam_mob2,"\n")
      escreva ("Quantidade Derrotada: ",mob_hunt,"\n")
      escreva ("Tempo da Hunt: ",hunt_time,"\n")
      escreva ("-------------------------------------------\n")
      escreva ("XP Total Ganho: ",(xp_mob2*mob_hunt),"\n")
      escreva ("GP Total Ganho: ", (gp_mob2*mob_hunt),"\n")
      escreva ("Peso estimado Loot: ",(oz_mob2*mob_hunt)," Oz\n")
      escreva ("-------------------------------------------\n")
      escreva ("Custo dos Suprimentos: ",(repot_price),"\n")
      escreva ("Lucro/Prejuiso Estimado: ",((gp_mob2*mob_hunt)-repot_price),"\n")
      escreva ("-------------------------------------------\n")
      escreva ("Média de XP por Hora: ",((xp_mob2*mob_hunt)/hunt_time),"\n")
      escreva ("Média de GP por Hora: ",((gp_mob2*mob_hunt)/hunt_time),"\n")
       escreva ("-------------------------------------------\n")
      escreva ("Bom jogo, ",char,"\n")
    }

    se (mob == nam_mob3) {
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
      escreva ("Monstro Focado: ", nam_mob3,"\n")
      escreva ("Quantidade Derrotada: ",mob_hunt,"\n")
      escreva ("Tempo da Hunt: ",hunt_time,"\n")
      escreva ("-------------------------------------------\n")
      escreva ("XP Total Ganho: ",(xp_mob3*mob_hunt),"\n")
      escreva ("GP Total Ganho: ", (gp_mob3*mob_hunt),"\n")
      escreva ("Peso estimado Loot: ",(oz_mob3*mob_hunt)," Oz\n")
      escreva ("-------------------------------------------\n")
      escreva ("Custo dos Suprimentos: ",(repot_price),"\n")
      escreva ("Lucro/Prejuiso Estimado: ",((gp_mob1*mob_hunt)-repot_price),"\n")
      escreva ("-------------------------------------------\n")
      escreva ("Média de XP por Hora: ",((xp_mob3*mob_hunt)/hunt_time),"\n")
      escreva ("Média de GP por Hora: ",((gp_mob3*mob_hunt)/hunt_time),"\n")
       escreva ("-------------------------------------------\n")
      escreva ("Bom jogo, ",char,"\n")
    }

    se (mob == nam_mob4) {
      escreva ("Nome do seu Personagem: ")
      leia (char)
      escreva ("Quantos ",nam_mob4,"(s) você derrotou? ")
      leia (mob_hunt)
      escreva ("Tempo total de caçada (em horas, exemplo: 1.5 para 1h 30): ")
      leia (hunt_time)
      escreva ("Custo total de suprimentos (poções, etc) em GPs: ")
      leia (repot_price)
      escreva ("\n")
      escreva ("--- Relatório da Caçada de ",char," ---\n")
      escreva ("Monstro Focado: ", nam_mob4,"\n")
      escreva ("Quantidade Derrotada: ",mob_hunt,"\n")
      escreva ("Tempo da Hunt: ",hunt_time,"\n")
      escreva ("-------------------------------------------\n")
      escreva ("XP Total Ganho: ",(xp_mob4*mob_hunt),"\n")
      escreva ("GP Total Ganho: ", (gp_mob4*mob_hunt),"\n")
      escreva ("Peso estimado Loot: ",(oz_mob4*mob_hunt)," Oz\n")
      escreva ("-------------------------------------------\n")
      escreva ("Custo dos Suprimentos: ",(repot_price),"\n")
      escreva ("Lucro/Prejuiso Estimado: ",((gp_mob4*mob_hunt)-repot_price),"\n")
      escreva ("-------------------------------------------\n")
      escreva ("Média de XP por Hora: ",((xp_mob4*mob_hunt)/hunt_time),"\n")
      escreva ("Média de GP por Hora: ",((gp_mob4*mob_hunt)/hunt_time),"\n")
       escreva ("-------------------------------------------\n")
      escreva ("Bom jogo, ",char,"\n")
    }

    senao {
      escreva ("Nome do mob não registrado ou escrito errado.")
    }
  }
}
