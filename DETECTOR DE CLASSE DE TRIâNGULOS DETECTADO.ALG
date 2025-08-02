Algoritmo "Detector de classe de triângulos detectado"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/07/2025
Var
// Seção de Declarações das variáveis 
esp,msg:caracter
esc1:logico
f1,f2,f3:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
esp <- "--------------------------------------------"
msg <- "|Detector de classe de triângulos detectado|"
Escreval(esp)
Escreval(msg)
Escreval(esp)
Escreva("Digite a área da primeira face do triangulo")
Escreva("R: ")
Leia(f1)

Escreva("Digite a área da segunda face do triangulo")
Escreva("R: ")
Leia(f2)

Escreva("Digite a área da terceira face do triangulo")
Escreva("R: ")
Leia(f3)

esc1 <- (f1<>f2)  e (f1<>f3) e (f2<>f3)


Escolha (esc1)
caso (esc1 = falso )
Escreval ("O triângulo é equilátero")
outrocaso


fimEscolha
Escreval (esc1)
Fimalgoritmo