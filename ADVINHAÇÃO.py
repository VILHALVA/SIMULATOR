from random import randint

def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError, IndexError):
            print("⛔VALOR INVÁLIDO!")
            continue
        else:
            return n

cont = 1
ROBO = randint(1,10)
print("😎Eu pensei no valor entre 1 e 10. Tente adivinhar qual é esse valor!")
while True:
    USUARIO = VALOR_INT(f"😎Qual é o seu [{cont}/3] Palpite?:\n>>>")
    cont += 1
    while USUARIO > 10 or USUARIO < 0:
        print("⛔VALOR INVÁLIDO!")
        USUARIO = VALOR_INT("🤬Qual é o seu palpite?\n>>>")
    if ROBO > USUARIO and cont < 4:
        print(f"😎ERRADO! O valor é maior do que {USUARIO}")
        continue
    elif ROBO < USUARIO and cont < 4:
        print(f"😎ERRADO! O valor é menor do que {USUARIO}")
        continue
    elif USUARIO != ROBO and cont == 4:
        print(f"😢Você perdeu! O valor era {ROBO}")
        break
    elif ROBO == USUARIO:
        print(f"⭐PARABÉNS! VOCÊ ACERTOU. O VALOR É {ROBO}")
        break
print("⛔FIM")
    
        


