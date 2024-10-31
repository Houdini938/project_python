# project_python

data_loader.py : Charge les fichiers de données et convertit les formats (ex., JSON vers DataFrame). On s’assure aussi d’avoir un format de date uniforme.

data_cleaning.py : Applique les étapes de nettoyage, comme le retrait des valeurs manquantes et la standardisation des champs de texte.

data_pipeline.py : Ordonne les étapes de la pipeline et applique la logique métier pour identifier les mentions de médicaments dans les titres.

graph_builder.py : Génère un graphe JSON en suivant la structure demandée. Ici, on applique les règles de gestion définies (mention dans un titre = mention dans l’article).

analysis.py : Implémente les fonctions bonus demandées pour l'analyse de données sur le graphe.
