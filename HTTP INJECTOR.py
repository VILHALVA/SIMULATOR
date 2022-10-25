from time import sleep
from random import randint
import webbrowser as wb

print("😎Esse jogo se trata de um simulador do HTTP injector com navegação!")
sleep(1)
            
while True:
    print("=" *120)
    print("             ⭐MENU DE IP:               ")
    print("-" *120)
    print('''
        A) 192.345.46.78
        B) 187.232.56.90
        C) 121.345.34.22
        D) 456.122.56.78
        E) 567.789.56.43
        F) 444.567.67.89
        G) 101.345.68.45
        H) 222.111.00.12
        I) 666.897.90.32
        J) 356.543.21.22''')
    print()
    print("=" *120)
    HTTP = randint(1,10)
    if HTTP == 1:
        CONEXAO = "A" 
        IPH = "192.345.46.78" 
    elif HTTP == 2:
        CONEXAO = "B"
        IPH = "187.232.56.90"
    elif HTTP == 3:
        CONEXAO = "C"
        IPH = "121.345.34.22"
    elif HTTP == 4:
        CONEXAO = "D"
        IPH = "456.122.56.78"
    elif HTTP == 5:
        CONEXAO = "E"
        IPH = "567.789.56.43"
    elif HTTP == 6:
        CONEXAO = "F"
        IPH = "444.567.67.89"
    elif HTTP == 7:
        CONEXAO = "G"
        IPH = "101.345.68.45"
    elif HTTP == 8:
        CONEXAO = "H"
        IPH = "222.111.00.12"
    elif HTTP == 9:
        CONEXAO = "I"
        IPH = "666.897.90.32"
    elif HTTP == 10:
        CONEXAO = "J"
        IPH = "356.543.21.22"
    
    print(f"⭐O IP DISPONIVEL É: [{IPH}]",end="\r")
    sleep(3)    
    USUARIO = input("😎Digite a letra correspondente ao IP:\n>>>").strip().upper()[0]
    while USUARIO not in "ABCDEFGHIJ":
        print("⛔VALOR INVÁLIDO")
        USUARIO = input("😎Digite a letra correspondente ao IP:\n>>>").strip().upper()[0]
    if USUARIO in "A":
        IP = "192.345.46.78"
    elif USUARIO in "B":
        IP = "187.232.56.90"
    elif USUARIO in "C":
        IP = "121.345.34.22"
    elif USUARIO in "D":
        IP = "456.122.56.78"
    elif USUARIO in "E":
        IP = "567.789.56.43"
    elif USUARIO in "F":
        IP = "444.567.67.89"
    elif USUARIO in "G":
        IP = "101.345.68.45"
    elif USUARIO in "H":
        IP = "222.111.00.12"
    elif USUARIO in "I":
        IP = "666.897.90.32"
    elif USUARIO in "J":
        IP = "356.543.21.22"
          
    if USUARIO != CONEXAO:
        print("🚀CONECTANDO...",end="\r")
        sleep(3)
        print("🔕FALHA NA CONEXÃO...",end="\r")
        sleep(2)
        print(f"⛔ERRO AO CONECTAR NO IP: {IP}")
        sleep(1)
        print("💎TENTE NOVAMENTE...",end="\r")
        sleep(2)
        continue
    
    elif USUARIO == CONEXAO:
        print("🚀CONECTANDO...",end="\r")
        sleep(3)
        print("📲AUTENTICANDO...",end="\r")
        sleep(3)
        print(f"✅SISTEMA CONECTADO COM SUCESSO NO IP: {IP}")
        sleep(2)
        print("=" *120)
        print("                   ⭐MENU DE SITES:                     ")
        print("-" *120)
        print('''
            A) GOOGLE
            B) YOUTUBE
            C) MUSIC
            D) WIKIPEDIA
            E) ADOBE COLOR
            F) EMOJIPEDIA
            G) VIDEOS
            H) LIKEDLN
            I) GITHUB
            J) TRADUTOR
            K) DIGITAR URL''')
        print()
        print("=" *120)
        sleep(1)
        INTERNAUTA = str(input("😎Digite a letra da opção para abrir o site:\n>>>")).strip().upper()[0]
        while INTERNAUTA not in "ABCDEFGHIJK":
            print("⛔OPÇÃO INVÁLIDA!")
            INTERNAUTA = str(input("😎Digite a letra da opção para abrir o site:\n>>>")).strip().upper()[0]
        if INTERNAUTA in "A":
            URL = "chrome://newtab/"
            SITE = "GOOGLE"
        elif INTERNAUTA in "B":
            URL = "https://www.youtube.com/"
            SITE = "YOUTUBE"
        elif INTERNAUTA in "C":
            URL = "https://music.youtube.com/"
            SITE = "MUSIC"
        elif INTERNAUTA in "D":
            URL = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"
            SITE = "WIKIPEDIA"
        elif INTERNAUTA in "E":
            URL = "https://color.adobe.com/pt/create/color-wheel"
            SITE = "ADOBE COLOR"
        elif INTERNAUTA in "F":
            URL = "https://emojipedia.org/"
            SITE = "EMOJIPEDIA"
        elif INTERNAUTA in "G":
            URL = "https://pt.savefrom.net/176/"
            SITE = "VIDEOS"
        elif INTERNAUTA in "H":
            URL = "https://www.linkedin.com/jobs/"
            SITE = "LIKEDLN"
        elif INTERNAUTA in "I":
            URL = "https://github.com/"
            SITE = "GITHUB"
        elif INTERNAUTA in "J":
            URL = "https://translate.google.com.br/?lfhs=2"
            SITE = "TRADUTOR"
        elif INTERNAUTA in "K":
            URL = str(input("😎Digite a URL:\n>>>")).strip()
            SITE = str(input("😎Digite o nome do site:\n>>>")).strip()
        print(f"🚀ABRINDO O '{SITE}'...",end="\r")
        sleep(2)
        print()
        print("✅URL EM EXECUÇÃO")
        wb.open(URL)
        for c in range(60, 0, -1):
            print(f"🚀CONECTADO [{c}]...",end="\r")
            sleep(1)         
        print("🛑DESCONECTANDO",end="\r")
        sleep(2)
        print("🛑DESCONECTADO!",end="\r")
        sleep(2)
        print("😑SEU TEMPO DE PLUGIN EXPIROU!")
        sleep(1)
        print("💚TENTE NOVAMENTE...",end="\r")
        sleep(2)
        continue

