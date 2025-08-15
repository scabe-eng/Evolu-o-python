if unidade := 1:
 print("Conversor de unidade de Medida")
 sub_unidade1 = int(input("Quer converter as medidas de: \n"
                          "1.Quilómetro (km) \n"
                          "2. Hectómetro (Hm) \n"
                          "3.Decâmetro (dam) \n"
                          "4. Metro (m) \n"
                          "5.Decimetro (Dm)\n"
                          "6.Centimwtro (cm) \n"
                          "7.Milímetro (mm) \nR:"))
 sub_unidade2 = int(input("Para: \n"
                          "1.Quilómetro (km) \n"
                          "2. Hectómetro (Hm) \n"
                          "3.Decâmetro (dam) \n"
                          "4. Metro (m) \n"
                          "5.Decimetro (Dm)\n"
                          "6.Centimwtro (cm) \n"
                          "7.Milímetro (mm) \nR:"))
#Condições para a unidade a ser convertida
 if sub_unidade1 == 1:
  uni_a_converter = "Quilómetro (km)"
  eq_em_m = 1000 
 if sub_unidade1 == 2: 
  uni_a_converter = " Hectómetro (Hm)"
  eq_em_m = 100
 if sub_unidade1 == 3:
  uni_a_converter = "Decâmetro (dam)"
  eq_em_m = 10
 if sub_unidade1 == 4:
  uni_a_converter = "Metro (m)"
  eq_em_m = 1
 if sub_unidade1 == 5:
  uni_a_converter = "Decimetro (Dm)"
  eq_em_m = 0.1
 if sub_unidade1 == 6:
  uni_a_converter = "Centimetro (cm)"
  eq_em_m = 0.01
 if sub_unidade1 == 7:
  uni_a_converter = "Milímetro (mm)"
  eq_em_m = 0.001
 #////////Condições para a unidade a converter//////
 if sub_unidade2 == 1:
  uni_convertida = "Quilómetro (km)"
  eq_em_mf = 0.001 
 if sub_unidade2 == 2: 
  uni_convertida = " Hectómetro (Hm)"
  eq_em_mf = 0.01
 if sub_unidade2 == 3:
  uni_convertida = "Decâmetro (dam)"
 eq_em_mf = 0.1
 if sub_unidade2 == 4:
  uni_convertida = "Metro (m)"
  eq_em_mf = 1
 if sub_unidade2 == 5:
  uni_convertida = "Decimetro (Dm)"
  eq_em_mf = 10
 if sub_unidade2 == 6:
  uni_convertida = "Centimetro (cm)"
  eq_em_mf = 100
 if sub_unidade2 == 7:
  uni_convertida = "Milímetro (mm)"
  eq_em_mf = 1000
 M1 = float(input(f"Pretende converter quantos {uni_a_converter} para {uni_convertida} ? \n R: "))
 M2 = M1 * eq_em_m
 MF = M2 * eq_em_mf
 print(f"{M1} {uni_a_converter} são iguais a {MF} {uni_convertida}  ")