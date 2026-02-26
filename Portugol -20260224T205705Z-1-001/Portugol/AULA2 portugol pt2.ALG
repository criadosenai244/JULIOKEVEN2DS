Algoritmo "aula2"

Var
senha , senhacadastrada : caractere
usuario , usuariocadastrado : caractere


Inicio
usuariocadastrado <- "JKeven"
senhacadastrada <- "123456"

escreval("qual � o usuario: ")
leia(usuario)
escreval("")
escreval("qual � a senha ;")
leia(senha)
escreval("")

  
se (senha <> senhacadastrada)entao
   escreval ("Senha Incorreta")
senao
     se (usuario <> usuariocadastrado)entao
        escreval ("Usuario Incorreta")
     senao
         escreval("Seja Bem Vindo")
fimse
fimse

Fimalgoritmo
'