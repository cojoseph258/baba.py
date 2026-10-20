"""Challenge 1 : retrouver toutes les positions de chaque lettre."""


def letter_indices(word):
    # Chaque lettre est une clé ; sa valeur est une liste de positions.
    positions = {}

    for index, letter in enumerate(word):
        if letter in positions:
            positions[letter].append(index)
        else:
            positions[letter] = [index]

    return positions


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(letter_indices(word))
