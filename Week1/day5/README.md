# Week 1 — Day 5 : Mini-Project Day

Les réponses sont rangées par rubrique Octopus. Chaque fichier Python se lance
séparément dans le terminal de VS Code, depuis la racine du dépôt.

| Travail | Fichier |
| --- | --- |
| Morpion à deux joueurs | `MiniProjects/tic_tac_toe.py` |
| Pendu (six erreurs) | `MiniProjects/hangman.py` |
| Challenges : 20 exercices | `Challenges/challenges.py` |
| Challenges #2 : motifs et analyse du tri | `Challenges/challenges_2.py` |
| Daily Challenge : tri et mot le plus long | `DailyChallenge/challenges.py` |
| Daily Challenge : paires de nombres | `DailyChallenge/advanced_algorithm.py` |
| Our First GUI : sapin en caractères | `OnlineLearning/first_gui.py` |
| Find Duplicates : doublons sans set | `OnlineLearning/find_duplicates.py` |

Exemple :

```bash
python3 Week1/day5/MiniProjects/tic_tac_toe.py
python3 Week1/day5/MiniProjects/hangman.py
python3 Week1/day5/Challenges/challenges.py
python3 Week1/day5/Challenges/challenges_2.py
python3 Week1/day5/DailyChallenge/challenges.py
python3 Week1/day5/DailyChallenge/advanced_algorithm.py
python3 Week1/day5/OnlineLearning/first_gui.py
python3 Week1/day5/OnlineLearning/find_duplicates.py
```

## Comprendre les réponses

- **Morpion** : la grille contient trois listes de trois cases. Une boucle
  alterne X et O ; les lignes, colonnes et diagonales déterminent le gagnant.
  Une case occupée ou une saisie incorrecte est refusée.
- **Pendu** : `random.choice` choisit un mot ; les lettres déjà proposées sont
  mémorisées. Une erreur ajoute une partie du corps. Une lettre répétée ou
  invalide ne consomme pas d'essai. Les espaces des expressions restent visibles.
- **Challenges** : chaque fonction porte le numéro de son exercice. La partie
  finale affiche les résultats des 20 exemples. `common_div` exclut 1 pour
  suivre l'exemple du cours ; `mypassword` contient 10 caractères, donc 10 étoiles.
- **Challenges #2** : les motifs utilisent des boucles. Les commentaires retracent
  toutes les valeurs importantes du tri fourni, dont le résultat est
  `[2, 12, 24, 233, 354]`. L'échange est placé trop tôt dans l'énoncé : ce code
  n'est pas un tri correct pour toutes les listes (contre-exemple expliqué).
- **Daily Challenge** : `without,hello,bag,world` devient
  `bag,hello,without,world`. Les mots les plus longs des trois exemples sont
  `Margaret's`, `forever.` et `Forgetfulness`. Une égalité conserve le premier.
- **Paires** : on conserve les nombres déjà vus et recherche leur complément.
  Chaque paire de valeurs est affichée une fois. `(1864, 1864)` exige deux
  occurrences. Le parcours est linéaire en moyenne, suivi du tri des résultats.

## Notions du Day 5

**Code propre** : noms explicites, présentation régulière, comportement prévisible
et fonctions réutilisables pour éviter les répétitions (DRY).

**Étapes d'un site** : recueillir les besoins, planifier, développer, mettre en
ligne, tester, promouvoir puis maintenir. En pratique, les tests interviennent
également avant la mise en ligne et pendant le développement.

## Vérification

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s Week1/day5/tests -v
```

Les tests couvrent les huit alignements du morpion pour les deux joueurs, une
partie gagnée, une partie nulle, les saisies invalides, le pendu gagné/perdu,
les lettres répétées, les exemples, les chaînes vides et les paires avec doublons.

Le quiz, le questionnaire personnel, les enregistrements de cours et la séance
sportive sont des éléments séparés du code ; leur présence ici ne signifie pas
qu'ils ont été accomplis.
