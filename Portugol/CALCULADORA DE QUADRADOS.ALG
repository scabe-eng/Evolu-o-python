Algoritmo "Calculadora de quadrados"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/07/2025



//Desenvolva um algoritmo que receba dois valores numéricos inteiros,
// calcule e mostre a soma do quadrado desses dois números.

Var
   // Seção de Declarações das variáveis
   num1,num2: inteiro
   esp,msg,expl,af1,af2:caracter
   r1,r2: inteiro
   res,qr1,qr2: real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   esp <- "----------------------------------"
   msg <- "|  Somador de quadrados iniciado |"
   af1 <- "Digite o primeiro número, a descobrir e somar o seu quadrado"
   af2 <- "Digite o segundo número, a descobrir e somar o seu quadrado"
   Escreval(esp)
   Escreval(msg)
   Escreval(esp)

   repita

      Escreval(af1)
      Escreva("R: ")
      Leia (r1)
      Se (r1 = 0) entao
         escreval("0 não tem um quadrado, selecione um número inteiro para prosseguir")
      fimSe
   ate (r1<0) ou ( r1>0)

   repita

      Escreval(af2)
      Escreva("R: ")
      Leia (r2)
      Se (r2 = 0) entao
         escreval("Esta calculadora apenas funciona com números inteiros")
         escreval("Seleciona u número deste conjunto para continuar")
      fimSe
   ate (r2<0) ou ( r2>0)
   qr1 <- r1^2
   qr2 <- r2^2
   res <- (qr1) + (qr2)
   Escreva("A soma dos quadrados de ",r1," ( que é",qr1,") e ",r2," (que é", qr2,") é igual a",res)

Fimalgoritmo
