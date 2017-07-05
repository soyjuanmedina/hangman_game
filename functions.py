"""All usual function used by script."""


def ask_for_letter():
    letter = input('¿Qué letra quieres probar?')
    return letter

def chek_letter(letter):
    if not letter.isalpha() or len(letter) > 1:
        print('Error: Debe introducir un sola letra y no debe se un número, pero eso si, has perdido un intento')
        return False
    else:
        return True

def letter_in_word(secret_word, solve_word, letter):
    positions = [i for i, char in enumerate(secret_word) if char == letter]
    for position in positions:
        solve_word[position] = secret_word[position]
    return solve_word

def play_hangman():
    attempts = 5
    secret_word = "casa"
    solve_word = []
    for x in range (0, len(secret_word)):
        solve_word.append('-')
    played_characters = []
    print('Vamos a jugar con esta palabra: ', solve_word)
    for x in range (0, attempts):
        letter = ask_for_letter()
        if chek_letter(letter):
            played_characters.append(letter)
            solve_word = letter_in_word(secret_word, solve_word, letter)
            if not '-' in solve_word:
                print('Bien hecho, la palabra era ' + secret_word)
                answer = input('¿Quieres volver a jugar? s/n')
                if answer == 's':
                    play_hangman()
                else:
                    break
            else:
                print('Letras pedidas: ', played_characters)
                print('Así llevas la palabra: ', solve_word)
    print('Lo siento, la palabra era ' + secret_word)
    answer = input('¿Quieres volver a jugar? s/n')
    if answer == 's':
        play_hangman()
