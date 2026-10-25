# Exercices XP — réponses rédigées

## 1. Introduction à l'analyse de données
L'analyse de données consiste à formuler une question, recueillir des observations, contrôler leur qualité, les organiser, puis les résumer et interpréter pour apporter une réponse étayée. Elle ne se limite pas à tracer des graphiques : il faut préciser la population, les unités, les valeurs absentes et les limites de la méthode.

Elle aide à décider à partir de faits vérifiables, à suivre une évolution et à repérer des anomalies. Une corrélation ne suffit toutefois pas à établir une causalité ; les biais de collecte et les erreurs de mesure peuvent fausser les conclusions.

Trois applications :
- Commerce : comparer les ventes par magasin et semaine pour adapter les stocks. Les volumes, promotions et retours doivent être pris en compte.
- Santé : étudier des données agrégées pour suivre des tendances et évaluer des interventions, avec des protocoles statistiques et une protection des données personnelles.
- Météorologie : exploiter des réanalyses et observations pour entraîner et évaluer des modèles de prévision. L'ECMWF a mis AIFS en exploitation le 25 février 2025, puis une version d'ensemble le 1er juillet 2025. Une prévision probabiliste permet d'apprécier l'incertitude et d'organiser une réponse proportionnée.

Sources : [ECMWF, 25 février 2025](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational), [ECMWF, 1er juillet 2025](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational). Cas approfondi dans le Daily Challenge.

## 6. Données structurées ou non structurées
| Source | Réponse | Justification |
| --- | --- | --- |
| Rapports financiers Excel | Structurées si organisées en tableaux | Colonnes, lignes et types définis ; les commentaires libres et images restent non structurés. |
| Photographies sociales | Non structurées | Pixels sans schéma métier explicite ; métadonnées séparées structurables. |
| Articles de presse | Non structurées pour leur contenu | Texte libre ; date, auteur et rubrique peuvent former une table. |
| Inventaire relationnel | Structurées | Schéma, clés, types et relations définis. |
| Entretiens enregistrés | Non structurées | Signal audio et discours libre ; métadonnées structurables. |

## 7. Transformer des sources non structurées
| Source | Méthode et schéma proposé | Raisonnement et contrôle |
| --- | --- | --- |
| Blogs de voyage | Extraire titre, date, auteur, lieux et activités ; table `article_id, date, lieu, activité, extrait_source`. | NLP/reconnaissance d'entités pour les lieux ; conserver le texte et valider les ambiguïtés géographiques. |
| Appels clients | Transcription horodatée, séparation des locuteurs, extraction des motifs et produits ; table `appel_id, début, fin, locuteur, texte, motif, confiance`. | La transcription rend la recherche possible ; vérifier les mots mal reconnus, les accents et le consentement. |
| Notes manuscrites | Numériser, appliquer une reconnaissance d'écriture, regrouper les idées ; table `note_id, auteur_si_connu, thème, idée, confiance, image_source`. | Contrôle humain des mots incertains et conservation de l'original pour traçabilité. |
| Tutoriel cuisine vidéo | Transcrire l'audio et repérer les étapes ; table `recette_id, étape, temps_vidéo, ingrédient, quantité, unité, durée`. | Croiser paroles, texte incrusté et gestes ; vérifier les unités, ingrédients implicites et étapes. |

Le résultat est une représentation partielle : conserver la provenance et les scores de confiance évite de confondre extraction automatique et vérité.
