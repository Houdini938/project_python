# Projet Python de Pipeline de Données

## Structure de Code et Organisation

### Modularité et Réutilisabilité
Le projet est structuré en plusieurs modules (`data_loader.py`, `data_cleaning.py`, `data_pipeline.py`, `graph_builder.py`, `analysis.py`). Cette modularité permet de séparer chaque fonctionnalité, rendant le code plus lisible et facile à maintenir. Chaque module a une responsabilité unique (chargement des données, nettoyage, construction de la pipeline, etc.), ce qui permet de réutiliser les fonctions dans d'autres projets ou pipelines de données.

### Structure en DAG
La structure choisie est pensée pour faciliter l'intégration dans un orchestrateur de type DAG (Directed Acyclic Graph) comme Airflow, où chaque étape du pipeline (chargement des données, nettoyage, construction du graphe, analyse) peut être définie comme un "task". Cela permet de contrôler, superviser et rejouer chaque étape du processus de manière indépendante. Les fonctions sont également conçues pour être stateless, ce qui les rend plus adaptées pour une exécution orchestrée.

### Encapsulation des Processus dans des Fonctions
Les processus clés comme `load_csv`, `clean_data`, `build_graph`, et `journal_with_most_drugs` sont encapsulés dans des fonctions dédiées. Cela permet d'isoler les traitements et de les tester individuellement, favorisant une meilleure maintenabilité et facilitant les tests unitaires. Cette encapsulation est cruciale pour garantir la robustesse du code en production.

## Étapes de Cleansing de la Data

Les données proviennent de diverses sources (fichiers CSV, JSON) avec potentiellement des formats hétérogènes. L'étape de "cleansing" ou de nettoyage est donc essentielle pour garantir la qualité des données en entrée, afin d'éviter des erreurs dans les étapes suivantes. Voici les étapes clés :

### Chargement et Normalisation des Formats
- Les données sont chargées depuis des fichiers CSV ou JSON via les fonctions `load_csv` et `load_json`. Ces formats peuvent varier entre les fichiers, il est donc important de standardiser les types de données.
- Par exemple, la colonne `date` est standardisée avec la fonction `standardize_date_format`, en convertissant toutes les dates au format ISO8601 (`YYYY-MM-DD`). Cela facilite les jointures et les filtrages par date.

### Suppression des Lignes Incomplètes
- Dans `clean_data`, nous supprimons les lignes contenant des valeurs `NaN` pour les colonnes essentielles telles que `title` et `journal`. Ces informations sont nécessaires pour identifier les sources et mentions de médicaments. En production, les lignes avec des valeurs nulles dans des colonnes clés peuvent fausser les analyses.

### Nettoyage et Uniformisation des Textes
- Les titres (`title`) sont transformés en majuscules pour normaliser les données textuelles, ce qui simplifie les recherches et les comparaisons ultérieures. Cela est utile pour éviter des cas d'incohérence liés à la casse du texte (ex: `aspirin` vs `Aspirin`).

### Gestion des Erreurs
- Le code utilise `errors='coerce'` dans `pd.to_datetime` pour gérer les dates incorrectes. Cette pratique permet de convertir les valeurs incorrectes en `NaT` (Not a Time), plutôt que de faire échouer le processus. En production, il est fréquent de rencontrer des données de mauvaise qualité ; cette approche permet de continuer le pipeline sans interrompre l'exécution.

## Bonnes Pratiques en Python et Conception de Jobs de Données

### Utilisation de Pandas
- `pandas` est utilisé pour manipuler les données en DataFrames, ce qui est optimal pour des manipulations de données tabulaires. Pandas fournit des méthodes de traitement vectorisé, permettant des manipulations rapides et efficaces sur de grandes quantités de données, ce qui est crucial dans un environnement de production.

### Respect des Conventions de Nommage
- Les noms de fonctions et de variables sont explicites et suivent les conventions de style Python (`snake_case`). Cela améliore la lisibilité du code et facilite la collaboration entre développeurs.

### Gestion des Exceptions et des Erreurs
- Dans un environnement de production, les exceptions sont gérées pour éviter les interruptions soudaines du processus de pipeline. Par exemple, dans le chargement des données, des vérifications sont faites pour s'assurer que les fichiers existent et que les formats sont corrects. Le fait de gérer les erreurs permet de créer des rapports d'anomalies pour identifier les fichiers ou lignes problématiques, sans arrêter le pipeline.

### Documentation et Tests Unitaires
- Le code est documenté et accompagné de tests unitaires, assurant une meilleure compréhension des objectifs de chaque fonction et facilitant leur maintenance.
- Les tests unitaires, écrits avec `pytest`, permettent de valider chaque fonction indépendamment. Ces tests vérifient le bon fonctionnement des étapes critiques (chargement, nettoyage, transformation) et garantissent la qualité du code lors de modifications ou de mises à jour.

### Optimisation des Performances
- Le code est optimisé pour des environnements de production en évitant les boucles sur les DataFrames, préférant des opérations vectorisées de Pandas qui sont bien plus performantes.
- Le projet utilise également des structures de données adaptées (comme les dictionnaires pour les graphes) qui sont efficaces pour effectuer des recherches et des opérations sur les données.

### Séparation des Responsabilités
- Le code suit le principe de séparation des responsabilités (Single Responsibility Principle), chaque module étant responsable d'une tâche spécifique. Cela permet de tester, déployer et réutiliser les modules indépendamment, ce qui est essentiel dans des environnements de pipeline de données complexes.
