from time import sleep
from random import randint
import webbrowser as wb

def QUESTAO(msg):
    print("=" *110)
    print(msg)
    print("=" *110)

def TEMPO():
    for c in range(60,0,-1):
        print(f"🛑AGUARDE [{c}]...",end="\r")
        sleep(1)
        
print("😎Esse é um pequeno jogo de Etiqueta: Cada Decisão que você tomar, terá que arcar com as conssequencias!") 
sleep(1)

cont = 0
while True:
    sleep(2)
    cont += 1
    ROBO = randint(1,100)   
    QUESTAO('''⭐PERGUNTA: Imagine a seguinte situação: Sua esposa está morrendo no hospital, e o tratamento dela custa R$ 80000,00; Você recebe uma proposta de trabalho em que poderá ganhar por dia 4 milhões de reais, mas tendo uma única condição: Terar que mentir para ocultar as merdas que o seu chefe faz. O que fazer?
        [ A ] Em nome da etiqueta regeitar essa proposta e deixar sua esposa morrer;
        [ B ] Largar a Etiqueta, e salvar sua esposa aceitando esse emprego;
        [ C ] Não aceitar esse emprego, mas apenas contar com a sorte de uma opurtunidade melhor cair do céu;
        [ D ] Aceitar o emprego para salvar sua esposa, mas revelar toda a merda que o seu chefe faz.''')
    sleep(1)
    USUARIO = str(input("😎O que você faria?\n>>>")).strip().upper()[0]
    while USUARIO not in "ABCD":
        print("⛔RESPOSTA INVALIDA!")
        USUARIO = str(input("😎O que você faria?\n>>>")).strip().upper()[0]
    if ROBO == 1 or ROBO > 20 and ROBO <= 50:
        LETRA = "A"
    elif ROBO == 2 or ROBO > 4 and ROBO <= 20:
        LETRA = "B"
    elif ROBO == 3 or ROBO > 50 and ROBO <= 70:
        LETRA = "C"
    elif ROBO == 4 or ROBO > 70 and ROBO <= 100:
        LETRA = "D"

    if USUARIO == LETRA:
        print(f"😎VOCÊ FOI NA OPÇÃO '{USUARIO}'. TAMBÉM CONCORDO COM VOCÊ!!!")
        sleep(1)
        if LETRA in "A":
            print("⭐SERIA UMA FALTA DE ETIQUETA VOCÊ ESPERAR SUA ESPOSA MORRER SEM VOCÊ FAZER NADA!")
        elif LETRA in "B":
            print("⭐NA REALIDADE QUANDO A CRISE VEM, NÃO HÁ IDEOLOGIA QUE SOBREVIVA!")
        elif LETRA in "C":
            print("⭐AS VEZES TEMOS QUE CONTAR COM A SORTE. E ESPERAR UMA OPORTUNIDADE MELHOR!")
        elif LETRA in "D":
            print("⭐VOCÊ PODERÁ GANHAR A CAUSA NA JUSTIÇA, E AINDA GANHAR DINHEIRO COM ISSO PARA AJUDAR SUA ESPOSA!")
        sleep(1)
        print("😑MUITO BEM! VOCÊ DEU SORTE!!!")
        break
    elif USUARIO != LETRA and USUARIO in "A":
        print("⛔VOCÊ PERDEU!!!")
        sleep(1)
        if cont == 1:
            print("🤬Em nome da etiqueta você deixaria sua esposa morrer?")
        elif cont == 2:
            print("🤬Acha melhor ser politicamente correto? E também ser um homicida?")
        elif cont == 3:
            print("🤬Se acha muito esperto né? Ser acusado de feminicidio!")
        elif cont == 4:
            print("🤬Em nome da Etiqueta, você teria o maior prazer em ver sua esposa morrer?")
        elif cont == 5:
            print("🤬Parece que você não dá a minima para a vida da sua mulher!")
        elif cont == 6:
            print("🤬Com um marido assim, quem precisa de inimigos?")
        elif cont == 7:
            print("🤬Os principios morais não paga suas contas. Acorda para a realidade!")
        elif cont == 8:
            print("🤬Está me parecendo que você é um psicopata!")
        elif cont == 9:
            print("🤬Eu acho que você é um caso perdido! Não consigo te convencer de geito nenhum!")
        elif cont >= 10:
            print("🤬JÁ CHEGA! VOCÊ IRÁ PEGAR UM MINUTO DE ESPERA!")
            TEMPO()
        sleep(1)
        continue
    elif USUARIO != LETRA and USUARIO in "B":
        print("⛔VOCÊ PERDEU!!!")
        sleep(1)
        if cont == 1:
            print("🤬Você irá contra seus principios morais apenas para salvar sua esposa?")
        elif cont == 2:
            print("🤬Sua mãe não te ensinou sobre honestidade?")
        elif cont == 3:
            print("🤬Não é atoa que muita gente se vende por uns trocados!")
        elif cont == 4:
            print("🤬Acredito que existe metodos melhores de salvar quem você ama sem se corromper!")
        elif cont == 5:
            print("🤬Você nunca pensou na possibilidade de montar seu proprio negocio?")
        elif cont == 6:
            print("🤬Você aceita ser mais um neste mar de corruptos?")
        elif cont == 7:
            print("🤬Seria muito melhor sua esposa partir logo. Afinal todo mundo irá morrer um dia!")
        elif cont == 8:
            print("🤬Me parece que você não entende nada de absolutos morais!")
        elif cont == 9:
            print("🤬Eu acho que você é um caso perdido! Não consigo te convencer de geito nenhum!")
        elif cont >= 10:
            print("🤬JÁ CHEGA! VOCÊ IRÁ PEGAR UM MINUTO DE ESPERA!")
            TEMPO()
        sleep(1)
        continue
    elif USUARIO != LETRA and USUARIO in "C":
        print("⛔VOCÊ PERDEU!!!")
        sleep(1)
        if cont == 1:
            print("🤬É serio isso? Você irá esperar outra oportunidade cair do céu?")
        elif cont == 2:
            print("🤬Você corre o risco grande perder alguém que ama, enquanto não faz nada!")
        elif cont == 3:
            print("🤬Que tipo de marido você é?")
        elif cont == 4:
            print("🤬Você não se preocupa em carregar uma morte dessas na sua consciência?")
        elif cont == 5:
            print("🤬Eu acho você está contando demais com a sorte, não acha?")
        elif cont == 6:
            print("🤬Você é Passivo Agressivo?")
        elif cont == 7:
            print("🤬Sua esposa está lá morrendo e você não faz nada?")
        elif cont == 8:
            print("🤬Se ela estivesse no seu lugar, você gostaria que ela te tratasse assim?")
        elif cont == 9:
            print("🤬Eu acho que você é um caso perdido! Não consigo te convencer de geito nenhum!")
        elif cont >= 10:
            print("🤬JÁ CHEGA! VOCÊ IRÁ PEGAR UM MINUTO DE ESPERA!")
            TEMPO()
        sleep(1)
        continue
    elif USUARIO != LETRA and USUARIO in "D":
        print("⛔VOCÊ PERDEU!!!")
        sleep(1)
        if cont == 1:
            print("🤬Você correria o risco de perder o caso na justiça pela quebra de contrato?")
        elif cont == 2:
            print("🤬Você daria conta de pagar as despesas judiciais?")
        elif cont == 3:
            print("🤬Você não tem medo de não ser mais contratado por ser dedo duro?")
        elif cont == 4:
            print("🤬Você não dá a minima pela sua reputação né?")
        elif cont == 5:
            print("🤬Eu não sei decidir se você é muito corajoso ou muito burro!")
        elif cont == 6:
            print("🤬Olha que você está brincando com fogo!")
        elif cont == 7:
            print("🤬Você irá pagar o maior mico se perder o caso!")
        elif cont == 8:
            print("🤬Lembre-se que o seu chefe é muito rico. Ele pode comprar o caso se quiser!")
        elif cont == 9:
            print("🤬Eu acho que você é um caso perdido! Não consigo te convencer de geito nenhum!")
        elif cont >= 10:
            print("🤬JÁ CHEGA! VOCÊ IRÁ PEGAR UM MINUTO DE ESPERA!")
            TEMPO()
        sleep(1)
        continue

if cont == 1:
    RESULTADO = "⭐PARABÉNS! VOCÊ VENCEU DE PRIMEIRA!!!"
elif cont > 1 and cont < 5:
    RESULTADO = "⭐MUITO BEM! ATÉ QUE NÃO FOI TÃO MAL ASSIM!"
elif cont > 5 and cont <= 10:
    RESULTADO = "⭐NOSSA! VOCÊ TEVE UM MAU DESEPENHO!"
elif cont > 10:
    RESULTADO = "🤬NOSSA! VOCÊ É BURRO PRA PORRA!"

print("-" *120)           
print(f"⭐VENCEU COM {cont} TENTATIVAS!!!")
print(RESULTADO)
print("⭐THE END!")
print("-" *120)
sleep(2)

if cont >= 1 and cont <= 5:
    print("😎Como você foi muito bom no Teste. Vou deixar você navegar no YOUTUBE!")
    sleep(1)
    print("✅ABRINDO O YOUTUBE...",end="\r")
    sleep(3)
    wb.open("https://www.youtube.com/")
    print("🚀YOUTUBE ESTÁ EM EXECUÇÃO!")
else:
    print("🤬Como você muito mal no Teste. Vou te obrigar a navegar na Wikipedia. Você precisa estudar mais!")
    sleep(1)
    print("✅ABRINDO A WIKIPEDIA...",end="\r")
    sleep(3)
    wb.open("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")
    print("🚀WIKIPEDIA ESTÁ EM EXECUÇÃO!")