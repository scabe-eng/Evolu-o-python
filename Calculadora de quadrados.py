A = print("====================================\n"
          "|       Calculadora iniciada       | \n"
          "====================================\n")
unidade = int(input("Selecione a unidade que deseja converter\n"
                    "1.Medida \n"
                    "2.Massa \nR:"
                    "3.Volume \nR:"))
if unidade == 1:
    import medida
if unidade == 2:
    import peso
if unidade == 3:

    import volume