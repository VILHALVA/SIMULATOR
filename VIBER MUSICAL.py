from random import randint

print("😁Eu gosto de umas musicas!")
while True:
    res = str(input("😎Você quer saber qual o meu gênero favorito[S/N]?\n>>>")).strip().upper()[0]
    while res not in "SN":
        print("⛔ERRO! RESPOSTA INVÁLIDA!")
        res = str(input("😡Basta apenas responder: Você quer SIM ou NÃO?\n>>>")).strip().upper()[0]
    if res in "Ss":
        VALOR = randint(1,10)
        if VALOR == 1:
            print("⭐EU CURTO SERTANEJO!")
        elif VALOR == 2:
            print("⭐EU GOSTO DE FORRÓ!")
        elif VALOR == 3:
            print("⭐EU GOSTO DE DANCE!")
        elif VALOR == 4:
            print("⭐EU GOSTO DE RAP!")
        elif VALOR == 5:
            print("⭐EU GOSTO DE JAZZ!")
        elif VALOR == 6:
            print("⭐EU GOSTO DE POP!")
        elif VALOR == 7:
            print("⭐EU GOSTO DE ÓPERA!")
        elif VALOR == 8:
            print("⭐EU GOSTO DE BREGA!")
        elif VALOR == 9:
            print("⭐EU GOSTO BLUES!")
        elif VALOR == 10:
            print("⭐EU GOSTO DE GOSPEL!")
    elif res in "Nn":
        break

print("🤬MUITO OBRIGADO POR ME USAR! ADEUS!")
