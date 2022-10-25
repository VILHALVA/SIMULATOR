from time import sleep
import webbrowser as wb

def menu (TITULO, OPCOES):
    print("=" *70)
    print(TITULO)
    print("-" *70)
    print(OPCOES)
    print("=" *70)
    
print("😎Iremos descobrir juntos qual é a sua tessitura vocal.")
sleep(1)
sexo = str(input("😎Qual é o seu sexo?[M/F]:\n>>>")).strip().upper()[0]
while sexo not in "MF":
    print("⛔RESPOSTA INVÁLIDA!")
    sexo = str(input("😡Você é HOMEM[M] ou MULHER[F]?:\n>>>")).strip().upper()[0]
if sexo in "M":
    menu("                          VOZ MASCULINA: ",'''
         [ A ] NOTAS E1 ATÉ E3 
         [ B ] NOTAS A1 ATÉ A3
         [ C ] NOTAS C2 ATÉ C4''')
    NOTA = str(input("😎Qual é a sua nota?\n>>>")).strip().upper()[0]
    while NOTA not in ("A", "B", "C"):
        print("⛔RESPOSTA INVÁLIDA!")
        NOTA = str(input("😡Qual é a nota que você alcança?\n>>>")).strip().upper()[0]
    if NOTA in "A":
        print("⭐SUA TESSITURA É 'BAIXO'!")
    elif NOTA in "B":
        print("⭐SUA TESSITURA É 'BARÍTONO'!")
    elif NOTA in "C":
        print("⭐SUA TESSITURA É 'TENOR'!")
elif sexo in "F":
    menu("                          VOZ FEMININA", '''
         [ D ] NOTAS F2 ATÉ F4 
         [ E ] NOTAS A2 ATÉ A4 
         [ F ] NOTAS C3 ATÉ C5''')
    NOTA = str(input("😎Qual é a sua nota?\n>>>")).strip().upper()[0]
    while NOTA not in ("D", "E", "F"):
        print("⛔RESPOSTA INVÁLIDA!")
        NOTA = str(input("😡Qual é a nota que você alcança?\n>>>")).strip().upper()[0]
    if NOTA in "D":
        print("⭐SUA TESSITURA É 'CONTRALTO'!")
    elif NOTA in "E":
        print("⭐SUA TESSITURA É 'MEZZO-SOPRANO'!")
    elif NOTA in "F":
        print("⭐SUA TESSITURA É 'SOPRANO'!")
        
WEB = str(input("😎Deseja aprender mais?\n>>>")).strip().upper()[0]
while WEB not in "SN":
    print("⛔RESPOSTA INVÁLIDA!")
    WEB = str(input("😡Você é quer aprender SIM ou NÃO?:\n>>>")).strip().upper()[0]
if WEB in "S":
    wb.open("https://www.descomplicandoamusica.com/classificacao-e-extensao-vocal/")
elif WEB in "N":
    print("⛔THE END!")
