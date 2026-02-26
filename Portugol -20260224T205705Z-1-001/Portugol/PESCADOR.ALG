Algoritmo "PESCADOR"

Var
Peso, excesso , Valordamulta : real
Inicio
escreval("Digite o peso do peixe")
leia(Peso)

  se (Peso > 50 )entao
    excesso <- Peso -  50
    Valordamulta <- excesso * 4

senao
   excesso <- 0
   Valordamulta <- 0
fimse
escreval("excesso: ", excesso)
escreval("Valormulta: R$ ", Valordamulta)
Fimalgoritmo