from time import sleep
from random import randint

print("😎Esse jogo consiste em perguntas e respostas pessoais para dupla de pessoas!")
sleep(1)

NOME = list()
NOTAS = list()

while True:
    TRANSMISSOR = randint(1,5)
    RECEPTOR = randint(1,5)
    if TRANSMISSOR == RECEPTOR:
        continue
    elif TRANSMISSOR == 1:
        PERGUNTE = "PESSOA 1" 
    elif TRANSMISSOR == 2:
        PERGUNTE = "PESSOA 2"
    elif TRANSMISSOR == 3:
        PERGUNTE = "PESSOA 3"
    elif TRANSMISSOR == 4:
        PERGUNTE = "PESSOA 4"
    elif TRANSMISSOR == 5:
        PERGUNTE = "PESSOA 5"

    if RECEPTOR == 1:
        RESPONDA = "PESSOA 1"
        NOME.append("PESSOA 1")
    elif RECEPTOR == 2:
        RESPONDA = "PESSOA 2"
        NOME.append("PESSOA 2")
    elif RECEPTOR == 3:
        RESPONDA = "PESSOA 3"
        NOME.append("PESSOA 3")
    elif RECEPTOR == 4:
        RESPONDA = "PESSOA 4"
        NOME.append("PESSOA 4")
    elif RECEPTOR == 5:
        RESPONDA = "PESSOA 5"
        NOME.append("PESSOA 5")
    
    print()
    print("=" *100)
    print(f">>> ⭐AGORA O {PERGUNTE} PERGUNTA PARA {RESPONDA} <<<")
    print("=" *100)
    print()
    
    ACERTOU = str(input(f"😎O {RESPONDA} ACERTOU[S/N]?\n>>>")).strip().upper()[0]
    while ACERTOU not in "SsNn":
        print("🛑RESPOSTA INVÁLIDA!")
        RES = str(input(f"😡O {RESPONDA} ACERTOU SIM OU NÃO?\n>>>")).strip().upper()[0]
    if ACERTOU in "Ss":
        NOTAS.append(+1)
    elif ACERTOU in "Nn":
        NOTAS.append(-1)

    RES = str(input("😎VOCÊ QUER CONTINUAR[S/N]?\n>>>")).strip().upper()[0]
    while RES not in "SsNn":
        print("🛑RESPOSTA INVÁLIDA!")
        RES = str(input("😡VOCÊ QUER CONTINUAR SIM OU NÃO?\n>>>")).strip().upper()[0]
    if RES in "Ss":
        continue
    elif RES in "Nn":
        break

for nome in enumerate(NOME): 
    for valor in enumerate(NOTAS):
        print(f"{nome} = {valor}")
