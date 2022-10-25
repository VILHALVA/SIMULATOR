from time import sleep
from random import randint

print("😎Esse jogo conssiste em perguntas e respostas pessoais para dupla de pessoas!")
sleep(1)

NOME = list()
NOTAS = list()

while True:
    TRANSMISSOR = randint(1,5)
    RECEPTOR = randint(1,5)
    if TRANSMISSOR == RECEPTOR:
        continue
    elif TRANSMISSOR == 1:
        PERGUNTE = "SAMUEL" 
    elif TRANSMISSOR == 2:
        PERGUNTE = "VALCILDA"
    elif TRANSMISSOR == 3:
        PERGUNTE = "HELIO"
    elif TRANSMISSOR == 4:
        PERGUNTE = "JAQUELINE"
    elif TRANSMISSOR == 5:
        PERGUNTE = "CAROLINE"

    if RECEPTOR == 1:
        RESPONDA = "SAMUEL"
        NOME.append("SAMUEL")
    elif RECEPTOR == 2:
        RESPONDA = "VALCILDA"
        NOME.append("VALCILDA")
    elif RECEPTOR == 3:
        RESPONDA = "HELIO"
        NOME.append("HELIO")
    elif RECEPTOR == 4:
        RESPONDA = "JAQUELINE"
        NOME.append("JAQUELINE")
    elif RECEPTOR == 5:
        RESPONDA = "CAROLINE"
        NOME.append("CAROLINE")
    
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
