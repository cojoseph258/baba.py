"""Quatre exercices sur les dictionnaires, avec les deux bonus."""

# Exercise 1: Converting Lists into Dictionaries
# zip() associe chaque clé à la valeur située au même index.
print("\nExercise 1: Lists into Dictionaries")
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)


# Exercise 2: Cinemax #2
print("\nExercise 2: Cinemax")
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name}: ${price}")
    total_cost += price

print(f"Total cost: ${total_cost}")


# Exercise 3: Zara
print("\nExercise 3: Zara")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"],
    },
}

brand["number_stores"] = 2
clothes = brand["type_of_clothes"]
print(f"Zara's clients are {', '.join(clothes[:3])}; "
      f"it also sells products for the {clothes[3]}.")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")
print("Last competitor:", brand["international_competitors"][-1])
print("US colors:", brand["major_color"]["US"])
print("Number of keys:", len(brand))
print("All keys:", list(brand.keys()))

# Bonus : update() ajoute les clés absentes et remplace les valeurs existantes.
# Le bonus ne précise pas les valeurs : on utilise 1975 et 10000.
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print("Merged dictionary:", brand)


# Exercise 4: Disney Characters
print("\nExercise 4: Disney Characters")
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# enumerate() fournit les couples (index, nom).
disney_users_A = {name: index for index, name in enumerate(users)}
disney_users_B = {index: name for index, name in enumerate(users)}
disney_users_C = {name: index for index, name in enumerate(sorted(users))}

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)


# Exercise 2 — Bonus interactif, placé à la fin pour voir les 4 résultats d'abord.
print("\nCinemax bonus: enter your family (blank name to finish).")
custom_family = {}

while True:
    name = input("Name: ").strip()
    if not name:
        break
    if name in custom_family:
        print("This name already exists. Use a different name.")
        continue

    while True:
        try:
            age = int(input(f"Age of {name}: "))
        except ValueError:
            print("Enter a whole number, for example 12.")
            continue
        if age < 0:
            print("Age cannot be negative.")
            continue
        break

    custom_family[name] = age

bonus_total_cost = 0
for name, age in custom_family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name}: ${price}")
    bonus_total_cost += price

print(f"Total cost for your family: ${bonus_total_cost}")
