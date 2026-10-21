# Week 1 — Day 4 : Functions

## Exercices XP

Les sept exercices de base se trouvent dans `ExercisesXP/functions.py`.
Depuis la racine du projet :

```bash
python3 Week1/day4/ExercisesXP/functions.py
```

Ils montrent les paramètres, les valeurs par défaut, les nombres aléatoires,
la modification d'une liste et les conditions dans une fonction.

Deux détails de l'énoncé sont ambigus : pour les magiciens, le code suit la
consigne « before » et place `the Great` avant le nom, même si l'exemple le met
après. Pour la température, les intervalles retenus sont : moins de 0, 0–15,
16–23, 24–32 et 33–40, afin de couvrir chaque entier une seule fois.

## Daily Challenge — Coffee Shop Menu Manager

```bash
python3 Week1/day4/DailyChallenge/coffee_shop.py
```

Choisir 1 pour afficher, 2 pour ajouter, 3 pour modifier le prix, 4 pour
supprimer et 5 pour quitter. Le menu initial contient espresso (7.0₪),
latte (12.0₪) et cappuccino (10.0₪). Les changements restent en mémoire :
ils disparaissent lorsque le programme se ferme.

Les fonctions reçoivent le dictionnaire et le modifient directement.
Un article existant n'est pas écrasé lors d'un ajout. Les articles absents
et les choix incorrects affichent les messages demandés.

Périmètre : exercices XP de base et Coffee Shop. Aucun Gold, Ninja ou bonus
facultatif n'est inclus.
