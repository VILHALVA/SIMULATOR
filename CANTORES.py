from time import sleep
from random import randint
import webbrowser as wb

def VALOR_INT(msg):
      while True:
            try:
                  n = int(input(msg))
            except(ValueError, TypeError, IndexError):
                  print("⛔VALOR INVÁLIDO!")
                  continue
            else:
                  return n
            
def ANALISE():
      for c in range(0,101,25):
            print(f"🚀PROCESSANDO({c})%...",end="\r")
            sleep(1)
            
def PLAY():
      for c in range(60,00,-1):
            print(f"💎PLAY({c})...",end="\r")
            sleep(1)

print("😎Olá! aqui iremos testar se um determido cantor pode ser executado através do metodo randomico!")
sleep(1)

while True:
    print("=" *120)
    print("           ⭐CANTORES DISPONIVIES:                   ")
    print("-" *120)
    print('''
          [ 0 ] SAIR DO PROGRAMA
          [ 1 ] ZEZÉ DI CAMARGO E LUCIANO
          [ 2 ] CLEITON E CAMARGO
          [ 3 ] CHINTÃOZINHO E XORORÓ
          [ 4 ] BANDA CALYPSO
          [ 5 ] OS LEVITAS
          [ 6 ] CANARINHOS DE CRISTO
          [ 7 ] DANIEL E SAMUEL
          [ 8 ] BRUNO E MARRONE
          [ 9 ] ZÉ RAMALHO
          [ 10 ] ROBERTA MIRANDA''')
    print("=" *120)
    sleep(1)
    A = randint(1,10)
    B = randint(1,10)
    Z = A + B
    print(f">A = {A} / >B = {B}",end="\r")
    sleep(3)
    res = VALOR_INT("😎Digite o número correspondente ao cantor:\n>>>") 
    while res < 0 or res > 10:
      print("⛔VALOR INVÁLIDO!")
      res = VALOR_INT("😎Digite o número correspondente ao cantor:\n>>>")
    
    if res == 0:
          break 
    elif A != res and B != res:
      ANALISE()
      if Z >= 1 or Z <= 10:
            print("⛔FORMATO INCOPATIVÉL!")
            sleep(2)
      elif Z > 10 or Z <= 20:
            print("⛔FORMATO NÃO SUPORTADO!")
            sleep(2)
      continue
    elif A == res or B == res:
          ANALISE()
          print("✅URL EM EXECUÇÃO")
          sleep(1)
          if res == 1:
                print("💚ABRINDO ZEZÉ DI CAMARGO E LUCIANO!")
                sleep(1)
                wb.open("https://www.youtube.com/c/zezedicamargoeluciano")
                PLAY()
                continue
          elif res == 2:
                print("💚ABRINDO CLEITON E CAMARGO!")
                sleep(1)
                wb.open("https://www.youtube.com/c/Cleitonecamargooficial")
                PLAY()
                continue
          elif res == 3:
                print("💚ABRINDO CHINTÃOZINHO E XORORÓ!")
                sleep(1)
                wb.open("https://www.youtube.com/c/chxoficial")
                PLAY()
                continue
          elif res == 4:
                print("💚ABRINDO BANDA CALYPSO!")
                sleep(1)
                wb.open("https://www.youtube.com/c/BandaCalypsoOficial")
                PLAY()
                continue
          elif res == 5:
                print("💚ABRINDO OS LEVITAS!")
                sleep(1)
                wb.open("https://www.youtube.com/c/Fl%C3%A1vioeKaiqueOficial")
                PLAY()
                continue
          elif res == 6:
                print("💚ABRINDO OS CANARINHOS DE CRISTO!")
                sleep(1)
                wb.open("https://youtu.be/F7vSeWbOcKc")
                PLAY()
                continue
          elif res == 7:
                print("💚ABRINDO DANIEL E SAMUEL!")
                sleep(1)
                wb.open("https://www.youtube.com/c/DanieleSamuelOficial")
                PLAY()
                continue
          elif res == 8:
                print("💚ABRINDO BRUNO E MARRONE!")
                sleep(1)
                wb.open("https://www.youtube.com/c/brunoemarrone")
                PLAY()
                continue
          elif res == 9:
                print("💚ABRINDO ZÉ RAMALHO!")
                sleep(1)
                wb.open("https://www.youtube.com/user/Zeramalho")
                PLAY()
                continue
          elif res == 10:
                print("💚ABRINDO ROBERTA MIRANDA!")
                sleep(1)
                wb.open("https://www.youtube.com/user/RobertaMirandaRM")
                PLAY()
                continue
print("🔕THE END!")
                
                
                
            
                

          
      
          
      
      