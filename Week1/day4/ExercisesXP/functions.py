"""Day 4 — Les sept exercices de base sur les fonctions."""

import random


# 1. Une fonction sans paramètre.
def display_message():
    print("I am learning about functions in Python.")


# 2. Un paramètre permet de réutiliser la fonction avec plusieurs livres.
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


# 3. La valeur par défaut est utilisée si le pays n'est pas fourni.
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")


# 4. randint inclut les deux bornes, 1 et 100.
def compare_number(number):
    if not 1 <= number <= 100:
        raise ValueError("Choose a number between 1 and 100.")
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")


# 5. On peut fournir des arguments ou garder les valeurs par défaut.
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")


# 6. La liste reçue est modifiée directement.
def show_magicians(magician_names):
    for name in magician_names:
        print(name)


def make_great(magician_names):
    for index in range(len(magician_names)):
        # On suit la consigne écrite : placer « the Great » avant le nom.
        magician_names[index] = "the Great " + magician_names[index]


# 7. Température entière entre -10 et 40, sans les bonus facultatifs.
def get_random_temp():
    return random.randint(-10, 40)


def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
    # Les bornes sont réparties sans chevauchement : 0–15, 16–23,
    # 24–32, puis 33–40.
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature <= 23:
        print("Nice weather.")
    elif temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


if __name__ == "__main__":
    print("\nExercise 1")
    display_message()
    print("\nExercise 2")
    favorite_book("Alice in Wonderland")
    print("\nExercise 3")
    describe_city("Reykjavik", "Iceland")
    describe_city("Paris")
    print("\nExercise 4")
    compare_number(50)
    print("\nExercise 5")
    make_shirt()
    make_shirt("medium")
    make_shirt("small", "Custom message")
    print("\nExercise 6")
    magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
    make_great(magician_names)
    show_magicians(magician_names)
    print("\nExercise 7")
    main()
