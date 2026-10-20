"""Challenge 2 : acheter dans l'ordre de priorité sans dépasser le budget."""


def affordable_items(items_purchase, wallet):
    # On enlève les symboles avant de convertir le montant en entier.
    wallet = int(wallet.replace("$", "").replace(",", ""))
    basket = []

    # Le dictionnaire conserve l'ordre de priorité des articles.
    for item, price in items_purchase.items():
        price = int(price.replace("$", "").replace(",", ""))
        if price <= wallet:
            basket.append(item)
            wallet -= price

    # On trie seulement le résultat, après avoir effectué les achats.
    if basket:
        return sorted(basket)
    else:
        return "Nothing"


if __name__ == "__main__":
    # Exemple 1
    items_purchase = {
        "Water": "$1",
        "Bread": "$3",
        "TV": "$1,000",
        "Fertilizer": "$20",
    }
    wallet = "$300"
    print(affordable_items(items_purchase, wallet))

    # Exemple 2
    items_purchase = {
        "Apple": "$4",
        "Honey": "$3",
        "Fan": "$14",
        "Bananas": "$4",
        "Pan": "$100",
        "Spoon": "$2",
    }
    wallet = "$100"
    print(affordable_items(items_purchase, wallet))

    # Exemple 3
    items_purchase = {
        "Phone": "$999",
        "Speakers": "$300",
        "Laptop": "$5,000",
        "PC": "$1200",
    }
    wallet = "$1"
    print(affordable_items(items_purchase, wallet))
