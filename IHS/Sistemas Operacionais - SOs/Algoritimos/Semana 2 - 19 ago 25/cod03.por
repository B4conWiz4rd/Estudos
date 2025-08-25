programa {
  funcao inicio() {
    cadeia n1,n2,n3, nome, err
    real s1,s2,s3
    
    n1 = "Edmilson"
    s1 = 1520.40
    n2 = "Fulano"
    s2 = 1620.45
    n3 = "Ciclano"
    s3 = 1720.32
    escreva ("Nome de funcionário: ")
    leia (nome)
    se (nome == n1) {
      escreva ("Funcionário: ",n1,"\n")
      escreva ("Salário: ",s1,"\n")
    }
    se (nome == n2) {
      escreva ("Funcionário: ",n2,"\n")
      escreva ("Salário: ",s2,"\n")
    }
    se (nome == n3) {
      escreva ("Funcionário: ",n3,"\n")
      escreva ("Salário: ",s3,"\n")
    }
  }
}
