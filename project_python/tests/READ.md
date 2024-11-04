test_data_loader.py : Teste le chargement des fichiers CSV/JSON et la standardisation des dates.

test_data_cleaning.py : Teste le nettoyage des données, y compris la suppression des valeurs nulles et la mise en majuscules des titres.

test_data_pipeline.py : Vérifie que les DataFrames de chaque source de données (drugs, pubmed, clinical_trials) ne sont pas vides après l'exécution de la pipeline.

test_graph_builder.py : Teste la construction du graphe pour s'assurer que les mentions de médicaments sont correctement ajoutées.

test_analysis.py : Teste les fonctions d'analyse pour identifier le journal le plus mentionné et les médicaments mentionnés dans les mêmes journaux.
