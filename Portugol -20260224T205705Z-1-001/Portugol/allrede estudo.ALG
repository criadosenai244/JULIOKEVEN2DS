Algoritmo "menu_opcao"

Var
   opcao : inteiro
   CPF, CPFcadastrado : caractere

Inicio
   escreval("Olá, sou a Assistente Virtual da Allrede Telecom.")
   escreval("1) Ver Ofertas")
   escreval("2) Já sou Cliente")
   escreva("Digite a opção desejada: ")
   leia(opcao)

   escolha(opcao)
      caso 1
         escreval("Ok, Digite o CPF: ")
         leia(CPF)

      caso 2
         escreval("Ok, Digite o CPF: ")
         leia(CPF)

      ooutrocaso
   escreval("Opção desejada incorreta.")
   fimescolha

   CPFcadastrado <- "08548109190"

   se (opcao = 1 ou opcao = 2) entao
      se (CPF = CPFcadastrado )entao
         escreval("CPF correta!")
         escreval("Seja bem-vindo Julio")
      senao
         escreval("CPF incorreta!")
         escreval("Tente novamente")
      fimse
   fimse

Fimalgoritmo
