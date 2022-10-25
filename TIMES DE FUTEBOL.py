def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError, IndexError):
            print("⛔Valor invalido!")
            continue
        else:
            return n
        
jogadores = dict()
partidas = list()

jogadores["nome"] = str(input("😎Digite o nome do jogador:\n>>>"))
tot = VALOR_INT(f"😎Quantas partidas '{jogadores['nome']}' jogou?\n>>>")
for c in range(0, tot):
    partidas.append(VALOR_INT(f"😎Quantos gols '{jogadores['nome']}' fez na {c+1}* partida?\n>>>"))
jogadores["gols"] = partidas[:]
jogadores["total"] = sum(partidas)

print("=" *100)
print(jogadores)
print("_" *100)

for k, v in jogadores.items():
    print(f"⭐O campo {k} tem o valor {v}")
print("_" *100)
print(f"⭐O jogador {jogadores['nome']} jogou {len(jogadores['gols'])} partidas:")
for i, v in enumerate(jogadores["gols"]):
    print(f"⭐Na {i+1} partidas fez {v} gols!")
print(f"⭐Foi o total de {jogadores['total']} gols!")
print("=" *100)