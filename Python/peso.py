if unidade := 2:
 print("Conversor de unidade de Medida")
 sub_unidade1 = int(input("Quer converter as medidas de: \n"
                          "1.Tonelada (T) \n"
                          "2.Quilograma (kg) \n"
                          "3. Hectograma (Hg) \n"
                          "4.Decâgrama (dag) \n"
                          "5. Grama (g) \n"
                          "6.Decigrama (Dg)\n"
                          "7.Centigrama (cg) \n"
                          "8.Miligrama (mg) \nR:"))
 sub_unidade2 = int(input("Para: \n"
                          "1.Tonelada (T) \n"
                          "2.Quilograma (kg) \n"
                          "3. Hectograma (Hg) \n"
                          "4.Decâgrama (dag) \n"
                          "5. Grama (g) \n"
                          "6.Decigrama (Dg)\n"
                          "7.Centigrama (cg) \n"
                          "8.Miligrama (mg) \nR:"))
#Condições para a unidade a ser convertida
 if sub_unidade1 == 1:
  uni_a_converter = "Tonelada (T)"
  eq_em_m = 1000000
 if sub_unidade1 == 2:
  uni_a_converter = "Quilograma (kg)"
  eq_em_m = 1000 
 if sub_unidade1 == 3: 
  uni_a_converter = " Hectograma (Hg)"
  eq_em_m = 100
 if sub_unidade1 == 4:
  uni_a_converter = "Decagrama (dag)"
  eq_em_m = 10
 if sub_unidade1 == 5:
  uni_a_converter = "Grama (g)"
  eq_em_m = 1
 if sub_unidade1 == 6:
  uni_a_converter = "Decigrama (Dg)"
  eq_em_m = 0.1
 if sub_unidade1 == 7:
  uni_a_converter = "Centigrama (cg)"
  eq_em_m = 0.01
 if sub_unidade1 == 8:
  uni_a_converter = "Miligrama (mg)"
  eq_em_m = 0.001
#////////Condições para a unidade a converter//////
 if sub_unidade2 == 1:
  uni_convertida = "Tonelada (T)"
  eq_em_mf = 1000000
 if sub_unidade2 == 2:
  uni_convertida = "Quilograma (kg)"
  eq_em_mf = 0.001 
 if sub_unidade2 == 3: 
  uni_convertida = " Hectograma (Hg)"
  eq_em_mf = 0.01
 if sub_unidade2 == 4:
  uni_convertida = "Decagrama (dag)"
  eq_em_mf = 0.1
 if sub_unidade2 == 5:
  uni_convertida = "Grama (g)"
  eq_em_mf = 1
 if sub_unidade2 == 6:
  uni_convertida = "Decigrama (Dg)"
  eq_em_mf = 10
 if sub_unidade2 == 7:
  uni_convertida = "Centigrama (cg)"
  eq_em_mf = 100
 if sub_unidade2 == 8:
  uni_convertida = "Miligrama (mg)"
  eq_em_mf = 1000
 M1 = float(input(f"Pretende converter quantos {uni_a_converter} para {uni_convertida} ? \n R: "))
 M2 = M1 * eq_em_m
 MF = M2 * eq_em_mf
 print(f"{M1} {uni_a_converter} são iguais a {MF} {uni_convertida}  ")
