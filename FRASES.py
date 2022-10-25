from random import randint
from time import sleep

def FRASE(msg):
    print("=" *120)
    print(">>>",msg,"<<<")
    print("=" *120)
    sleep(1)
    print()

cont = 1
while True:
    ROBO = randint(1,10)
    cont += 1
    if ROBO == 1:
        FRASE("⭐Toda adversidade representa uma opurtunidade de aprendizado!")
    elif ROBO == 2:
        FRASE("⭐A vida é mais do que o dinheiro pode comprar!")
    elif ROBO == 3:
        FRASE("⭐Somos mais do que produtores e consumidores!")
    elif ROBO == 4:
        FRASE("⭐A diversão está na jornada, não no destino!")
    elif ROBO == 5:
        FRASE("⭐Sem amor a vida não tem graça!")
    elif ROBO == 6:
        FRASE("⭐Devemos presentiar a pessoa durante sua vida, não após a sua morte")
    elif ROBO == 7:
        FRASE("⭐Só valorizamos algo quando perdemos!")
    elif ROBO == 8:
        FRASE("⭐Não somos donos do próprio destino!")
    elif ROBO == 9:
        FRASE("⭐É preciso apanhar para aprender a bater!")
    elif ROBO == 10:
        FRASE("⭐Não existe trabalho ruim, o ruim é ter que trabalhar!")
    RES = str(input(f"😠Você quer ler a {cont}* Frase?[S/N]\n>>>")).strip().upper()[0]
    while RES not in "SsNn":
        print("🛑RESPOSTA INVÁLIDA!")
        RES = str(input("😡É só responder: SIM ou NÃO?\n>>>")).strip().lower()[0]
    if RES in "Ss":
        continue
    elif RES in "Nn":
        break
print("🛑THE END")