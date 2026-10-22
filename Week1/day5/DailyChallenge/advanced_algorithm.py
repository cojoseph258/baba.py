"""Trouver les paires de valeurs distinctes dont la somme vaut la cible."""
import random


def find_pairs(numbers, target):
    seen = set()
    pairs = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.add(tuple(sorted((number, complement))))
        seen.add(number)
    # Un doublon comme (1864, 1864) exige deux occurrences dans la liste.
    return sorted(pairs)


if __name__ == "__main__":
    list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
    target_number = 3728
    for first, second in find_pairs(list_of_numbers, target_number):
        print(f"{first} + {second} = {target_number}")
