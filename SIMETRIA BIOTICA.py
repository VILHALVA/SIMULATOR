def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print("Valor invalido!")
            continue
        else:
            return n
        
A = VALOR_INT("Digite o valor do A:\n>>>")
B = VALOR_INT("Digite o valor de B:\n>>>")
C = VALOR_INT("Digite o valor de C:\n>>>")

if A >= B and A >= C:
    Z = (A * B * C) / 3 * 4
elif B >= A and B >= C:
    Z = (A * B * C) / 6 * 8
elif C >= A and C >= B:
    Z = (A * B * C) / 12 * 16

if Z > 0 and Z < 100:
    TIPO = "UNINÁRIO"    
elif Z >= 100 and Z <= 1000:
    TIPO = "BINÁRIO"
elif Z > 1000 and Z <= 10000:
    TIPO = "TERNÁRIO"
elif Z > 10000 and Z <= 50000:
    TIPO = "QUARTENÁRIO"
elif Z > 50000 and Z <= 10000000000:
    TIPO = "DECTARNÁRIO"
else:
    TIPO = "NULO"
    
print("_" *40)    
print(f"Calculando: [{A}],[{B}],[{C}];\nO valor de Z é {Z:.2f}\nO Tipo é {TIPO}")
print("_" *40)

while True:
    res = str(input("Voçe quer digitar o VETOR?\n>>>")).strip().upper()[0]
    if res in "Ss":
        VT = VALOR_INT("Digite o valor do VETOR:\n>>>")
        VETOR = (Z / VT * 8 **2) + 10 * 26 
        if VETOR >= Z:
            TYPO = "DIRETAMENTE PROPORCIONAL"
        elif VETOR < Z:
            TYPO = "INVERSAMENTE PROPORCIONAL"
        print("_" *40)
        print(f"Com o VETOR: {VT}\nSeu valor é {VETOR:.2f}\nSua grandeza é {TYPO}!")
        print("_" *40)
        break
    elif res in "Nn":
        break
    else:
        print("Resposta invalida!")

print("THE END")
        