"""Coffee Shop Menu Manager — menu en mémoire et fonctions réutilisables."""

menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}


def show_menu(menu_dict):
    """Afficher les boissons et leurs prix."""
    if not menu_dict:
        print("The menu is empty.")
    else:
        print("Current menu:")
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")


def add_item(menu_dict):
    """Ajouter une boisson sans écraser un article existant."""
    name = input("Enter new drink name: ").strip().lower()
    if name in menu_dict:
        print("Item already exists!")
        return
    if not name:
        print("Invalid name.")
        return
    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid price.")
        return
    menu_dict[name] = price
    print(f'"{name}" added!')


def update_price(menu_dict):
    """Modifier uniquement le prix d'une boisson existante."""
    name = input("Which drink do you want to update? ").strip().lower()
    if name not in menu_dict:
        print("Item not found.")
        return
    try:
        price = float(input("Enter the new price: "))
    except ValueError:
        print("Invalid price.")
        return
    menu_dict[name] = price
    print("Price updated!")


def delete_item(menu_dict):
    """Supprimer une boisson du dictionnaire."""
    name = input("Which drink do you want to delete? ").strip().lower()
    if name in menu_dict:
        del menu_dict[name]
        print("Item deleted.")
    else:
        print("Item not found.")


def show_options():
    print("\nWhat would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")


def run_coffee_shop():
    """La boucle choisit l'action ; chaque fonction réalise sa tâche."""
    while True:
        show_options()
        choice = input("> ").strip()
        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_price(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    run_coffee_shop()
