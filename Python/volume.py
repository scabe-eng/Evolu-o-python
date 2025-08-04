if unidade := 3:
    print("Conversor de unidade de Volume")
    sub_unidade1 = int(input("Quer converter as medidas de: \n"
                             "1. Quilolitro (kl)\n"
                             "2. Hectolitro (hl)\n"
                             "3. Decalitro (dal)\n"
                             "4. Litro (l)\n"
                             "5. Decilitro (dl)\n"
                             "6. Centilitro (cl)\n"
                             "7. Mililitro (ml)\nR: "))
    sub_unidade2 = int(input("Para: \n"
                             "1. Quilolitro (kl)\n"
                             "2. Hectolitro (hl)\n"
                             "3. Decalitro (dal)\n"
                             "4. Litro (l)\n"
                             "5. Decilitro (dl)\n"
                             "6. Centilitro (cl)\n"
                             "7. Mililitro (ml)\nR: "))
    # Condições para a unidade a ser convertida
    if sub_unidade1 == 1:
        uni_a_converter = "Quilolitro (kl)"
        eq_em_l = 1000
    if sub_unidade1 == 2:
        uni_a_converter = "Hectolitro (hl)"
        eq_em_l = 100
    if sub_unidade1 == 3:
        uni_a_converter = "Decalitro (dal)"
        eq_em_l = 10
    if sub_unidade1 == 4:
        uni_a_converter = "Litro (l)"
        eq_em_l = 1
    if sub_unidade1 == 5:
        uni_a_converter = "Decilitro (dl)"
        eq_em_l = 0.1
    if sub_unidade1 == 6:
        uni_a_converter = "Centilitro (cl)"
        eq_em_l = 0.01
    if sub_unidade1 == 7:
        uni_a_converter = "Mililitro (ml)"
        eq_em_l = 0.001
    # Condições para a unidade a converter
    if sub_unidade2 == 1:
        uni_convertida = "Quilolitro (kl)"
        eq_em_lf = 0.001
    if sub_unidade2 == 2:
        uni_convertida = "Hectolitro (hl)"
        eq_em_lf = 0.01
    if sub_unidade2 == 3:
        uni_convertida = "Decalitro (dal)"
        eq_em_lf = 0.1
    if sub_unidade2 == 4:
        uni_convertida = "Litro (l)"
        eq_em_lf = 1
    if sub_unidade2 == 5:
        uni_convertida = "Decilitro (dl)"
        eq_em_lf = 10
    if sub_unidade2 == 6:
        uni_convertida = "Centilitro (cl)"
        eq_em_lf = 100
    if sub_unidade2 == 7:
        uni_convertida = "Mililitro (ml)"
        eq_em_lf = 1000
    V1 = float(input(f"Pretende converter quantos {uni_a_converter} para {uni_convertida} ? \nR: "))
    V2 = V1 * eq_em_l
    VF = V2 * eq_em_lf
    print(f"{V1} {uni_a_converter} são iguais a {VF} {uni_convertida} ")
