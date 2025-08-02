Algoritmo "Conversor de unidades"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/07/2025
Var
   // Seção de Declarações das variáveis
   esp,msg,m1c,m2c:caracter
   ri,r1,r2,r1c,r2c:inteiro
   R1c2,R2c2,R3c2: real
   V1Bc,V2Bc: real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   esp <- "--------------------------------"
   msg <- "|Conversor de unidades iniciado|"
   Escreval("Este conversor de unidades pode calcular todas as medidas ")
   Escreval("Selecione a opção de medidas a converter (acompanhadas da")
   Escreval("unidade principal no S.I.")










   Escreval("                   Unidades de Medida Fundamentais(Base)do (SI):|")
   Escreval("")
   Escreval(" 1- Comprimento: Metro (m)")
   Escreval(" 2- Massa: Quilograma (kg)               |")
   Escreval(" 3- Tempo: Segundo (s)                   |")
   Escreval(" 4- Corrente Elétrica: Ampère (A)        |")
   Escreval(" 5- Temperatura Termodinâmica: Kelvin (K)|")
   Escreval(" 6-Qnt. d Substância:Mol (mol)           |")
   Escreval(" 7- Intensidade Luminosa: Candela (cd)   |")
   Escreval("**----------------------**---------**----------**-|")
   Escreval("                   Unidades de Medida Derivadas (Exemplos):    |")
   Escreval("")
   Escreval(" 8-  Volume: Metro cúbico (m³)           |")
   Escreval(" 9- Área: Metro quadrado (m²)            |")
   Escreval(" 10- Velocidade: Metro por segundo (m/s) |")
   Escreval("11- Força: Newton (N)                    |")
   Escreval("12-Energia: Joule (J)                    |")
   Escreval("13- Potência: Watt (W)                   |")
   Escreval("Digite 14 para sair")
   //Repetição caso erro
   repita
      //Mensagem de erro
      Escreval ("R: ")
      Leia  (ri)


      Se (ri<1) e (ri>13) entao
         escreval("Opção inválida, selecione uma opção válida")
      fimse


      Se (ri = 14) entao
Fimalgoritmo
fimse




ate (ri>=1) e (ri<=14)

//Opções resultantes de cada opção









//P/ Comprimento
//"Se for 1 // Se (ri = 1) entao
limpatela
escreval ("Converter medidas de comprimento!!")


//Condição de erro
repita
   escreval("De:")
   escreval("1- Metro(m) 2-Quilómetro(Km) 3.Hectómetro(hm) 4.Decâmetro(dm)")
   escreval("5.Decimetro(dcm)   6.Centimetro(cm)  7.Milímetro(mm)   8.sair")



   Leia (r1c)
   Se (r1c<1) ou (r1c>8) entao
      limpatela
      escreval("Opção anterior iválida, selecione uma das abaixo exibidas")
   fimSe
fimfuncao

ate (r1c >=1) e (r1c <= 8)






//Condição de erro
repita
   escreval("Para:")
   escreval("1. Metro(m) 2.Quilómetro(Km) 3.Hectómetro(hm) 4.Decâmetro(dm)")
   escreval("5.Decimetro(dcm)             6.Centimetro(cm) 7.Milímetro(mm)")
   Leia (r2c)
   Se (r2c<1) ou (r2c>7) entao
      limpatela
      escreval("Opção anterior iválida, selecione uma das abaixo exibidas")
   fimSe
ate (r2c >0) e (r2c < 8)




Se (r1c = 1 ) entao
   m1c <- "Metro (m)"
   V1Bc <- 1
fimSe
Se (r1c = 2 ) entao
   m1c <- "Quilómetros (Km)"
   V1Bc <- 1000
fimSe
Se (r1c = 3 ) entao
   m1c <- "Hectómetros (hm)"
   V1Bc <- 100
fimSe
Se (r1c = 4 ) entao
   m1c <- "Decâmetros (dam)"
   V1Bc <- 10
fimSe
Se (r1c = 5 ) entao
   m1c <- "Decímetros (dcm)"
   V1Bc <- 0.1
fimSe
Se (r1c = 6 ) entao
   m1c <- "Centímetros (cm)"
   V1Bc <- 0.01
fimSe
Se (r1c = 7 ) entao
   m1c <- "Milímetros (mm)"
   V1Bc <- 0.001
fimSe




Se (r2c = 1 ) entao
   m2c <- "Metro (m)"
   V2Bc <- 1
fimSe
Se (r2c = 2 ) entao
   m2c <- "Quilómetros (Km)"
   V2Bc <- 0.001
fimSe
Se (r2c = 3 ) entao
   m2c <- "Hectómetros (hm)"
   V2Bc <- 0.01
fimSe
Se (r2c = 4 ) entao
   m2c <- "Decâmetros (dam)"
   V2Bc <- 0.1
fimSe
Se (r2c = 5 ) entao
   m2c <- "Decímetros (dcm)"
   V2Bc <- 10
fimSe
Se (r2c = 6 ) entao
   m2c <- "Centímetros (cm)"
   V2Bc <- 100
fimSe
Se (r2c = 7 ) entao
   m2c <- "Milímetros (mm)"
   V2Bc <- 1000
fimSe





Escreval("Quer converter quantos ",m1c," para ",m2c)
Escreva("R: ")
Leia (R1c2)


//Converte o valor inserido acima para a unidade base
//Multiplica o resultado , pelo equivalente a 1 unidade da unidade
//a converter, com valor expresso na unidade base
R2c2 <- R1c2 * V1Bc
R3c2 <- R2c2 * V2Bc





//Escreve o resultado
Escreva(R1c2," ",m1c," equivalem a ",R3c2," ",m2c)
// Fim do "Se for a opção 1" // fimse



Fimalgoritmo