Algoritmo "semnome"

Var
nomes : vetor[1..3] de caractere
bimestreN1 : vetor[1..3] de real
bimestreN2 : vetor[1..3] de real
bimestreN3 : vetor[1..3] de real
 i : inteiro
 mediaFinal : vetor[1..3] de real
Inicio
para i<- 1 ate 3 faca
 escreval("qual é o nome do",i,"°aluno")
 leia(nomes[i])
 escreval("qual foi a nota no Primeiro bimestre")
 leia(bimestreN1[i])
 escreval("qual foi a nota no Segundo bimestre")
 leia(bimestreN2[i])
 escreval("qual foi a nota no Terceiro bimestre")
 leia(bimestreN3[i])
  limpatela
  mediaFinal[i] <- (bimestreN1[i]+bimestreN2[i]+bimestreN3[i])/3
  fimPara
 para i<- 1 ate 3 faca
  se (mediaFinal[i] >= 7) entao
   escreval(nomes[i], " APROVADO")
   escreval("________________________")
   senao
    escreval(nomes[i]," REPROVADO")
    escreval("_______________________")
    
 fimse
 fimpara

Fimalgoritmo