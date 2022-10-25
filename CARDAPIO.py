from random import randint
from time import sleep

print('''
    a) PIZZA
    b) SORVETE
    c) BOLO
    d) BISCOITO
    e) SADUICHE
    f) PICOLÉ
    g) BANANA
    h) MELÂNCIA
    i) CHOCOLATE
    j) MAMÃO''')
sleep(1)

ROBO = randint(1,10)
if ROBO == 1:
    COMER = "PIZZA"
    LETRA = "a"
    DICA = "SALGADO, QUENTE E REDONDO!"
elif ROBO == 2:
    COMER = "SORVETE"
    LETRA = "b"
    DICA = "DOCE E GELADO!"
elif ROBO == 3:
    COMER = "BOLO"
    LETRA = "c"
    DICA = "DOCE, GRANDE E BEM RECHEADO!"
elif ROBO == 4:
    COMER = "BISCOITO"
    LETRA = "d"
    DICA = "DOCE, PEQUENO E RECHEADO!"
elif ROBO == 5:
    COMER = "SANDUICHE"
    LETRA = "e"
    DICA = "PÃO COM PRESUNTO"
elif ROBO == 6:
    COMER = "PICOLÉ"
    LETRA = "f"
    DICA = "FRIO, FINO E DOCE"
elif ROBO == 7:
    COMER = "BANANA"
    LETRA = "g"
    DICA = "FRUTA AMARELO E SEM SEMENTES"
elif ROBO == 8:
    COMER = "MELÂNCIA"
    LETRA = "h"
    DICA = "FRUTA DOCE E VERMELHO"
elif ROBO == 9:
    COMER = "CHOCOLATE"
    LETRA = "i"
    DICA = "FEITO COM CACAU E LEITE CONDESSADO"
elif ROBO == 10:
    COMER = "MAMÃO"
    LETRA = "j"
    DICA = "FRUTA ALARANJADA E DOCE"

TENTO = 0
while True:
    print(f"😠TENTATIVAS: [{TENTO+1}/3]")
    USUARIO = str(input("😎Tente adivinhar o que eu quero comer hoje:\n>>>")).strip().lower()[0]
    TENTO += 1
    while USUARIO not in "abcdefghij":
        print("🛑RESPOSTA INVÁLIDA!")
        USUARIO = str(input("😡Escreva apenas a letra correspondente a opção:\n>>>")).strip().lower()[0]
    if USUARIO != LETRA and TENTO < 3:
        print(f"😡VOCÊ ERROU! A DICA É {DICA}")
        continue
    elif USUARIO != LETRA and TENTO == 3:
        print(f"😡VOCÊ PERDEU! EU QUERO COMER {COMER}!")
        exit()
    elif USUARIO == LETRA:
        print(f"⭐VOCÊ ACERTOU!\n⭐EU QUERO COMER: {COMER}!")
        exit()