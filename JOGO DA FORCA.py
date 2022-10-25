from random import choice
import os

colors = {'red': '\033[1;31m',
          'green': '\033[1;32m',
          'blue': '\033[1;36m',
          'gray': '\033[1;90m',
          'reset': '\033[m'}

def get_wordlist():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'WORD.txt')) as w:
            lines = w.readlines()
            words = [line.strip().upper() for line in lines]
            secret = choice(words)
            return secret
    except IOError:
        return "🛑ERRO: Nenhum dicionário foi encontrado."

def hide(word, masked, hack=False):
    for position, letter in enumerate(word):
        if masked[position] == letter:
            print(f'{colors["green"]}{letter}{colors["reset"]}', end=' ')
        elif word[position] == ' ':     
            masked[position] = letter   
            print('', end='')
        else:
            print('_', end=' ')
    print('', end='')
    print()
    if hack:
        for letter in word:
            print(f'{colors["gray"]}{letter.lower()}{colors["reset"]}', end=' ')
        print()

def play(secret):
    hidden = ['_' for letter in secret]
    guessed_letters = []
    turns = 6
    while turns > 0:
        hide(secret, hidden)
        if ''.join(secret) == ''.join(hidden):
            print("😃Parabéns, você acertou!")
            break
        print()
        guess = input("😎Tente adivinhar qual é a palavra secreta! Digite uma letra:\n>>>").strip().upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("🤨Você já jogou esta letra!")
            else:
                if guess in secret:
                    for position, letter in enumerate(secret):
                        if guess == letter:
                            hidden[position] = letter
                else:
                    turns -= 1
                    print(f"😠Errado! {colors['red']}{guess.upper()}{colors['reset']} não está na palavra.")
                guessed_letters.append(guess)
            if turns > 0:
                print(f"😎Letras jogadas: {colors['blue']}{' - '.join(guessed_letters)}{colors['reset']}")
                print(f"🤬Você tem {colors['red']}{turns}{colors['reset']} chance(s) restantes.")
        else:
            print("👽Você deve digitar uma letra.")
        print()
    else:
        print(f"😡Você perdeu! A resposta correta era {colors['red']}{secret}{colors['reset']}")

def main():
    word = get_wordlist()
    play(word)
if __name__ == '__main__':
    main()
