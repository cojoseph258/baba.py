# Exercise 1: Favorite Numbers

my_fav_numbers = {7, 10, 15}

my_fav_numbers.add(20)
my_fav_numbers.add(25)

my_fav_numbers.remove(25)

friend_fav_numbers = {5, 10, 30}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

# Exercise 2: Tuple

my_tuple = (1, 2, 3)

# Tuples cannot be modified directly
# We create a new tuple instead

my_tuple = my_tuple + (4, 5)

print(my_tuple)

# Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

print(basket.count("Apples"))

basket.clear()

print(basket)

# Exercise 4: Floats

numbers = []

for i in range(3, 11):
    number = i / 2

    if number.is_integer():
        number = int(number)

    numbers.append(number)

print(numbers)

# Exercise 5: For Loop

# Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Print numbers at even indexes
print("Numbers at even indexes:")

for index, number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)

        # Exercise 6: While Loop

while True:
    name = input("Enter your name: ")

    if len(name) >= 3 and name.isalpha():
        print("Thank you!")
        break
    else:
        print("Invalid name. Please try again.")

        # Exercise 7: Favorite Fruits

favorite_fruits = input("Enter your favorite fruits: ").lower().split()

fruit = input("Enter a fruit: ").lower()

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

    # Exercise 8: Pizza Toppings

toppings = []

while True:
    topping = input("Enter a pizza topping (or quit): ")

    if topping.lower() == "quit":
        break

    toppings.append(topping)

    print(f"Adding {topping} to your pizza.")

total = 10 + len(toppings) * 2.50

print("Your toppings:", toppings)
print(f"Total price: ${total:.2f}")

# Exercise 9: Cinemax Tickets

total = 0

while True:
    age_input = input("Enter age (or quit): ")

    if age_input.lower() == "quit":
        break

    if not age_input.isdigit():
        print("Invalid age. Try again.")
        continue

    age = int(age_input)

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total += price

    print(f"Ticket price: ${price}")

print(f"Total ticket cost: ${total}")