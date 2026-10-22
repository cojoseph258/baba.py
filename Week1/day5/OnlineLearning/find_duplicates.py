"""Trouver les doublons avec une boucle, sans utiliser de set."""


def find_duplicates(items):
    duplicates = []
    for item in items:
        if items.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates


if __name__ == "__main__":
    # Exemple d'application : chaque doublon n'apparaît qu'une fois.
    print(find_duplicates(['a', 'b', 'c', 'b', 'd', 'n', 'n']))
