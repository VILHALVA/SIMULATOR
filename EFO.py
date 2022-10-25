from time import sleep

def VALOR_FLOAT(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError, IndexError):
            print("⛔VALOR INVÁLIDO!")
            continue
        else:
            return n

print("😁Esse código foi criado para o calculo do comprimento de onda de luz copuscular: Constante de Planck!")
sleep(1)

while True:
    print('''        ⭐MENU PRINCIPAL: 
        [ 0 ] SAIR DO PROGRAMA    
        [ 1 ] COMPRIMENTO DE ONDA
        [ 2 ] CONSTANTE DE PLANCK''')
    res = VALOR_FLOAT("😎Qual equação você deseja usar?\n>>>")
    while res < 0 or res > 2:
        print("⛔ERRO! VALOR INVÁLIDO!")
        res = VALOR_FLOAT("😎Qual equação você deseja usar?\n>>>")
    if res == 0:
        break
    elif res == 1:
        h = VALOR_FLOAT("😎Digite a constante 'h' do campo:\n>>>")
        f = VALOR_FLOAT("😎Digite a constante 'f' do campo:\n>>>")
        E = ((h**7) * (f**8))
        print(f"⭐Calculando {h} e {f} o resultado é {E}!")
    elif res == 2:
        h = VALOR_FLOAT("😎Digite o valor 'h':\n>>>")
        m = VALOR_FLOAT("😎Digite o valor de 'm':\n>>>")
        v = VALOR_FLOAT("😎Digite o valor de 'v':\n>>>")
        E = h / m * v
        print(f"⭐Calculando {h}, {m} e {v} o resultado é {E}!")

print("🤬MUITO OBRIGADO POR ME USAR! ADEUS!")





