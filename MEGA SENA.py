from time import sleep
from random import randint

def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError, IndexError):
            print("🛑VALOR INVÁLIDO!")
            continue
        else:
            return n

lista = list()
jogos = list()

print("=" *100)
print("        JOGO DA MEGASENA:            ")
print("=" *100)

valor = VALOR_INT("😎Quantos jogos pretende jogar?\n>>>")
while valor < 1 or valor > 100:
    print("😡SINTO MUITO! O VALOR PRECISA SER ENTRE 1 E 100!")
    valor = VALOR_INT("😎Quantos jogos pretende jogar?\n>>>")
tot = 1
while tot <= valor:
    cont = 1
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 7:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-" *5, f"SORTEANDO {valor} JOGOS:", "-" *5)
print("=" *100)
for i, l in enumerate(jogos):
    print(f"⭐ {i+1} JOGO: {l}")
    sleep(1)
print("=" *100)
print("-" *5, "    BOA SORTE    ", "-" *5)


