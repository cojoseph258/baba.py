"""Motifs avec des boucles et analyse du tri fourni par l'énoncé."""


def draw_patterns():
    for row in range(3):
        print(" " * (2 - row) + "*" * (2 * row + 1))
    print()
    for row in range(1, 6):
        print(" " * (5 - row) + "*" * row)
    print()
    for row in range(1, 6):
        print("*" * row)
    for row in range(5, 0, -1):
        print(" " * (5 - row) + "*" * row)


def analyse_sort():
    my_list = [2, 24, 12, 354, 233]  # Liste initiale : cinq entiers.
    for i in range(len(my_list) - 1):  # i prend 0, 1, 2, puis 3.
        minimum = i  # Indice candidat, réinitialisé à chaque tour externe.
        for j in range(i + 1, len(my_list)):  # Explore les éléments suivants.
            if my_list[j] < my_list[minimum]:  # Compare deux valeurs.
                minimum = j  # Retient l'indice du nombre plus petit.
                if minimum != i:  # Ici vrai, car j est toujours supérieur à i.
                    # Échange immédiatement, comme dans le code de l'énoncé.
                    my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
    print(my_list)  # Résultat de cet exemple : [2, 12, 24, 233, 354].
    return my_list


# Trace avant exécution :
# i=0 : minimum=0 ; j=1,2,3,4 ; aucun échange.
# i=1 : minimum=1 ; j=2 -> minimum=2 -> [2,12,24,354,233].
#       j=3 et j=4 : aucune nouvelle valeur plus petite que my_list[2]=24.
# i=2 : minimum=2 ; j=3,4 ; aucun échange.
# i=3 : minimum=3 ; j=4 -> minimum=4 -> [2,12,24,233,354].
# Fin : i=3, j=4, minimum=4.
# Intention : trier en ordre croissant. Attention : l'échange est mal placé
# pour un tri par sélection général ; [3,1,2] donne [2,3,1] avec ce code.
# Un tri par sélection correct échange après la boucle sur j.

if __name__ == "__main__":
    draw_patterns()
    analyse_sort()
