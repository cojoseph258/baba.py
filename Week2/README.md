# Week 2 — Data Analysis : exercices standards

Consignes Octopus du cours 812, consultées le 29 octobre 2026. Les nouveaux livrables couvrent les jours 2 à 5 ; le jour 1 est déjà disponible dans [day1/ExercisesXP](day1/ExercisesXP).

| Jour | Exercices XP | Défi / projet |
|---|---|---|
| 1 | [10 exercices existants](day1/ExercisesXP/exercises_xp.ipynb) | Défis déjà dans day1/DailyChallenge |
| 2 | [7 exercices Titanic](day2_xp.ipynb) | [Salaires : normalisation, PCA, agrégation](day2_daily_salary.ipynb) |
| 3 | [8 exercices SciPy, dont 2 optionnels standards](day3_xp.ipynb) | [Accidents aériens](day3_daily_crashes.ipynb) |
| 4 | [6 exercices de visualisation](day4_xp.ipynb) | [Diagnostic Superstore et widgets](day4_daily_superstore.ipynb) |
| 5 | [Mini-projet marketing](day5_mini_project.ipynb) | [Visualisations interactives](day5_daily_interactive.ipynb) |

## Utilisation

Les 8 nouveaux notebooks sont autonomes : ils téléchargent les données publiques du cours dans `data/`. Installer les bibliothèques de `requirements.txt`, ouvrir le notebook dans Jupyter ou Google Colab et exécuter toutes les cellules dans l’ordre. Les résultats et graphiques de l’exécution vérifiée sont conservés dans chaque fichier. `validation.json` rapporte 8 exécutions réussies. Les widgets nécessitent un noyau actif ; des graphiques statiques sont aussi inclus pour la lecture sur GitHub.

## Points clés

- Titanic : imputation documentée, conservation des valeurs initiales, traitement des extrêmes avant mise à l’échelle et encodage des groupes d’âge. En modélisation, apprendre les transformations sur le train uniquement.
- Salaires : agrégation par expérience et devise ; ne pas comparer des monnaies différentes sans conversion. La PCA utilise les colonnes réellement présentes et affiche la variance retenue.
- Accidents : les taux de survie excluent les données incohérentes ou manquantes. Le nombre d’accidents recensés n’est pas un taux de risque par vol.
- Superstore : les décisions marketing tiennent compte du profit et de la marge, pas seulement des ventes ; les remises élevées sont à auditer, sans conclusion causale automatique.
- Le jeu US Superstore ne couvre que les États-Unis : la carte interactive respecte cette limite.

Aucun nouvel exercice Gold ou Ninja n’est ajouté. Les anciens dossiers Gold/Ninja du jour 1 préexistaient à cette intervention et sont conservés.
