# EXERCICE 1 : CONDITIONS

name = input("What is your name? ")

if len(name) < 5:
    print("You have a short name :)")

    # EXERCICE 2 : FIZZBUZZ

number = int(input("Enter a number between 1 and 100: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")