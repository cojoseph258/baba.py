"""Jeu du pendu : six erreurs maximum, sans répéter une lettre."""
import random

WORDS = ['correction', 'childish', 'beach', 'python', 'assertive',
         'interference', 'complete', 'share', 'credit card', 'rush', 'south']


def masked_word(word, guessed):
    # Les espaces restent visibles pour les expressions comme « credit card ».
    return "".join(letter if letter in guessed or letter == " " else "*"
                   for letter in word)


def display_hangman(errors):
    head = "O" if errors >= 1 else " "
    body = "|" if errors >= 2 else " "
    left_arm = "/" if errors >= 3 else " "
    right_arm = "\\" if errors >= 4 else " "
    left_leg = "/" if errors >= 5 else " "
    right_leg = "\\" if errors >= 6 else " "
    print(f" +---+\n |   {head}\n |  {left_arm}{body}{right_arm}\n |  {left_leg} {right_leg}\n===")


def play():
    word = random.choice(WORDS)
    guessed = []
    errors = 0
    while errors < 6:
        display_hangman(errors)
        print(masked_word(word, guessed))
        letter = input("Devine une lettre : ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Entre une seule lettre.")
            continue
        if letter in guessed:
            print("Tu as déjà proposé cette lettre.")
            continue
        guessed.append(letter)
        if letter not in word:
            errors += 1
        if "*" not in masked_word(word, guessed):
            print(f"Gagné ! Le mot était : {word}")
            return True
    display_hangman(errors)
    print(f"Perdu ! Le mot était : {word}")
    return False


if __name__ == "__main__":
    play()
