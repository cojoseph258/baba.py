# Daily Challenge — Une décision opérationnelle fondée sur l'analyse de données

## Cas choisi et chronologie
Le 25 février 2025, l'ECMWF a mis en exploitation son système de prévision météorologique par apprentissage automatique AIFS, aux côtés de son système physique IFS. Le 1er juillet 2025, il a ajouté AIFS ENS, un ensemble de 51 prévisions. Ce cas montre comment l'évaluation des données peut faire passer un prototype à un service opérationnel. Il est documenté par l'organisme qui exploite le système, avec une étude scientifique publiée en 2026 sur AIFS Single 1.1.0.

## Données et méthodes
Les modèles apprennent les évolutions atmosphériques à partir de réanalyses historiques, qui combinent observations et modèles physiques pour représenter l'état passé de l'atmosphère. Les variables incluent les champs atmosphériques et de surface ; une évaluation séparée compare ensuite les prévisions avec des références et des observations. L'apprentissage de régularités historiques relève de l'analyse prédictive. Les comparaisons d'erreurs par échéance, variable et événement servent à vérifier la performance hors des cas d'apprentissage.

L'ensemble fournit plusieurs trajectoires possibles : on étudie ainsi une distribution plutôt qu'une valeur unique. C'est pertinent lorsque des décisions dépendent du risque d'un événement extrême. La performance ne se réduit pas à un score moyen : résolution, fiabilité, précipitations et phénomènes extrêmes doivent aussi être examinés.

## Résultat et décision
L'organisme rapporte des améliorations allant jusqu'à 20 % sur certaines mesures pour les versions lancées en 2025 ; ce chiffre n'est ni une amélioration universelle ni une réduction garantie des pertes économiques. La décision concrète a été de mettre AIFS en exploitation en complément d'IFS. La version d'ensemble de juillet 2025 avait une résolution de 31 km contre 9 km pour l'ensemble physique : cette différence explique pourquoi les deux systèmes restaient complémentaires.

La réduction importante du coût de calcul des prévisions permet de produire davantage de scénarios. Une collectivité pourrait, par exemple, utiliser la probabilité de fortes pluies pour préparer des équipes. Il s'agit d'une application possible, pas d'un résultat économique mesuré dans les sources.

## Pourquoi l'analyse compte
Sans évaluation quantitative sur des données indépendantes, une prévision visuellement convaincante pourrait masquer des erreurs systématiques. Les mesures fournissent un critère pour décider du déploiement et repérer les limites. L'analyse contribue aussi à communiquer l'incertitude, afin de ne pas présenter un scénario comme certain.

Une performance historique n'assure pas une fiabilité parfaite : événements rares, changement climatique et différences de résolution exigent une surveillance continue. Le cas illustre une décision guidée par des preuves et accompagnée d'un système complémentaire, plutôt qu'une confiance sans contrôle dans un algorithme.

## Sources
- [ECMWF — AIFS devient opérationnel, 25 février 2025](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational).
- [ECMWF — Prévisions d'ensemble, 1er juillet 2025](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational).
- [Moldovan et al. — AIFS Single 1.1.0, GMD 2026](https://gmd.copernicus.org/articles/19/4703/2026/).

Analyse rédigée le 25 octobre 2026. Les chiffres cités se rapportent aux lancements 2025 ; le rapport ne les attribue pas aux versions actuelles.
