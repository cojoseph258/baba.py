# Week 2 — Day 1 : Data Analysis

Consignes : Octopus, cours 812, section 2143, consultées le 25 octobre 2026.

| Rubrique | Livrable | Contenu |
| --- | --- | --- |
| XP (10 exercices) | `ExercisesXP/exercises_xp.ipynb` + `ExercisesXP/reponses.md` | Chargement sommeil/santé mentale/crédit, classification de chaque colonne, Iris, observations sommeil, structure, transformations proposées, Titanic, exports Excel/JSON, import JSON URL. |
| Gold (6 exercices) | `ExercisesXPGold/exercises_gold.ipynb` | Statistiques Titanic, ventes/avis, e-commerce, trafic, MovieLens 20M, 500 produits Faker. |
| Ninja (5 exercices) | `ExercisesXPNinja/exercises_ninja.ipynb` | EDA assurance selon les étapes du tutoriel, Titanic, Iris, ventes/tickets, structuration de tweets. |
| Daily Challenge | `DailyChallenge/real_world_analysis.md` | Cas réel documenté ECMWF/AIFS. |
| Daily Challenge images | `DailyChallenge/image_transformations.ipynb` | Original, rotation 30°, miroirs, zoom ×1,2 et vérifications. |

Le notebook XP fonctionne seul et télécharge automatiquement ses données : voir `ExercisesXP/README.md` pour l’ouverture directe dans Google Colab. Les autres notebooks utilisent les fichiers communs du dossier.

Les notebooks contiennent les résultats exécutés et les graphiques. `results/` contient les exports, tables, données nettoyées et images ; `results/validation.json` indique les exécutions réussies.

## Refaire l'exécution
Depuis ce dossier :

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python download_data.py
.venv/bin/python run_notebooks.py
```

Dans VS Code, ouvrir les notebooks et sélectionner ce même environnement Python. Le dossier `data/` contient les données téléchargées ; il est ignoré par Git car MovieLens seul dépasse 600 Mo une fois décompressé. Le script les retélécharge à partir des chemins dans `datasets.json`. Les données du cours sont des archives Git LFS : le script utilise leur contenu binaire, pas le fichier pointeur.

Les fichiers du cours portent encore le nom « Week 4 » dans leurs URL ; ils correspondent néanmoins aux liens de la Week 2 actuelle. L'archive MovieLens contient `rating.csv` au singulier et les images commencent par `0001.png` : les solutions suivent les fichiers disponibles. Les en-têtes génériques du cours ne correspondent pas toujours à ses tâches numérotées ; celles-ci guident les réponses.

Les analyses distinguent code numérique et mesure, texte libre et catégorie, et association et causalité. Les vidéos, quiz, déclarations de progression, soumissions sur Octopus et publication GitHub ne sont pas effectués par ces fichiers.
