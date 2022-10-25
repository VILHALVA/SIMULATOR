from random import randint

print("😁Olá! Eu irei prever o clima com base no random entre 1 e 4!")
while True:
    usuario = str(input("😎Você quer saber a previsão do tempo agora[S/N]?\n>>>")).strip().upper()[0]
    while usuario not in "SN":
        print("⛔ERRO! RESPOSTA INVÁLIDA!")
        usuario = str(input("😡Basta apenas responder: Você quer SIM ou NÃO?\n>>>")).strip().upper()[0]
    if usuario in "Ss":
        robo = randint(1,4)
        if robo == 1:
            print("🌞 > DIA SERÁ ENSOLARADO!")
            continue
        elif robo == 2:
            print("🌥️  > DIA SERÁ NUBLADO!")
            continue
        elif robo == 3:
            print("🌧️  > DIA SERÁ CHUVOSO!")
            continue
        elif robo == 4:
            print("🌨️  > DIA SERÁ DE NEVASCA!")
            continue
    elif usuario in "Nn":
        break
print("🤬MUITO OBRIGADO POR ME USAR! ADEUS!")
