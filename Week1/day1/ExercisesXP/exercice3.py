# Exercise 1: Hello World
# Print "Hello world" four times using one line of code.

print("Hello world\n" * 4, end="")

# Exercise 2: Some Math

result = (99 ** 3) * 8

print(result)

# Exercise 3: What is the output?

# My guess: False
print(5 < 3)

# My guess: True
print(3 == 3)

# My guess: False
print(3 == "3")

# My guess: TypeError
try:
    print("3" > 3)
except TypeError:
    print("TypeError")

# My guess: False
print("Hello" == "hello")

# Exercise 4: Your Computer Brand

computer_brand = "Apple"

print(f"I have a {computer_brand} computer.")

# Exercise 5: Your Information

name = "Joseph"
age = 20
shoe_size = 42

info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."

print(info)

# Exercise 6: A & B

a = 20
b = 10

if a > b:
    print("Hello World")

    # Exercise 7: Odd or Even

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

    # Exercise 8: What's Your Name?

my_name = "Joseph"

user_name = input("What is your name? ")

if user_name.lower() == my_name.lower():
    print("Wow! We have the same name! Are we twins?")
else:
    print("Nice name! But Joseph is still the best!")

    # Exercise 9: Roller Coaster

height = int(input("What is your height in cm? "))

if height > 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("Sorry, you need to grow a little more to ride!")
    