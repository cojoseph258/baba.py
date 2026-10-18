description = "strings are..."

print(description.upper())
print(description.replace("are", "is"))
print(description[:7])


# EXERCICE 2 : NUMBERS

my_age = 21
future_age = my_age + 123879

print(future_age)

# EXERCICE 3 : TYPE CASTING

bank_balance = "33000"
phone_number = 532287514

# Afficher les types actuels
print(type(bank_balance))
print(type(phone_number))

# Convertir les types
bank_balance = int(bank_balance)
phone_number = str(phone_number)

# Afficher les nouveaux types
print(type(bank_balance))
print(type(phone_number))

# EXERCICE 4 : FIRST NAME / LAST NAME

first_name = "Joseph"
last_name = "Cohen"

full_name = first_name + " " + last_name

print(full_name)

# EXERCICE 5 : BOOLEANS

x = 5
y = 10
z = 0

word1 = "hello"
word2 = "world"

# 1. Comparer les nombres
print(x < y and y > z)

# 2. Vérifier si les mots sont différents
print(word1 != word2)

# 3. Vérifier les valeurs booléennes
print(bool(z))
print(bool(word1))