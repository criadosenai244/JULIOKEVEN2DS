Algoritmo "NADADOR"

Var
resposta : Caractere
opcao : inteiro
nome : caractere
nadador : Caractere
InfantilA : inteiro
InafntilB : inteiro
JuvenilA  : inteiro
JuvenilB  : inteiro
Adultos : inteiro
INICIO
escreval ("Olá Atleta, Tudo Bem??")
 leia(opcao)
 escreval("")
escreval ("Qual é o seu nome??")
  leia(nome)
  escreval("")
escreval ("Quantos anos você tem ??")
  leia(opcao)
escreval("1) Infantil A = 5 a 7 anos")
escreval("2) Infantil B = 8 a 11 anos")
escreval("3) Juvenil A = 12 a 13 anos")
escreval("4) Juvenil B = 14 a 17 anos")
escreval("5) Adultos = Maiores de 18 anos")
  leia(opcao)
  
escolha(opcao)
escreval("")
           Caso 1
             escreval("OK,Você está na categoria (Infantil A)")
           Caso 2
             escreval("OK,Você está na categoria (Infantil B)")
           Caso 3
             escreval("OK, Você está na categoria (Juvenil A)")
           Caso 4
             escreval("OK,Você está na categoria (Juvenil B)")
           Caso 5
             escreval("OK,Você está na categoria (Adultos)")
           outrocaso
      escreval("Erro! Opção inválida")

fimEscolha

Fimalgoritmo