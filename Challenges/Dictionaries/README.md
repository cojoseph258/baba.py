# Challenges — Dictionnaires

Un fichier par challenge, avec des commentaires en français.

## Challenge 1 — Positions des lettres

Depuis la racine du projet `baba.py` :

```bash
python3 Challenges/Dictionaries/challenge_1_letter_indices.py
```

Saisis un mot lorsque le programme le demande. Avec `dodo`, le résultat est :

```text
{'d': [0, 2], 'o': [1, 3]}
```

Les positions commencent à zéro. `enumerate()` donne la position et la lettre.
Si la lettre existe déjà dans le dictionnaire, `append()` ajoute sa nouvelle
position à sa liste. Sinon, une nouvelle liste est créée. La casse est conservée.

## Challenge 2 — Panier selon le budget

```bash
python3 Challenges/Dictionaries/challenge_2_affordable_items.py
```

Les trois exemples de l'énoncé sont exécutés :

```text
['Bread', 'Fertilizer', 'Water']
['Apple', 'Bananas', 'Fan', 'Honey', 'Spoon']
Nothing
```

`replace()` retire les dollars et les virgules, puis `int()` convertit le prix.
Les achats suivent l'ordre du dictionnaire : chaque achat réduit le budget
restant. Un article trop cher est ignoré et on passe au suivant. Le panier est
trié alphabétiquement uniquement après les achats. Un panier vide donne `Nothing`.

Tu peux modifier les dictionnaires et les budgets des exemples pour essayer
d'autres situations. Le bloc `if __name__ == "__main__":` lance les exemples
seulement lorsque le fichier est exécuté directement.
