def build_graph(drugs_df, pubmed_df, clinical_trials_df):
    graph = {}
    for _, drug in drugs_df.iterrows():
        mentions = []
        
        # Check for mentions in PubMed
        for _, article in pubmed_df.iterrows():
            if drug['drug'] in article['title']:
                mentions.append({'journal': article['journal'], 'date': article['date'], 'source': 'PubMed'})

        # Check for mentions in Clinical Trials
        for _, trial in clinical_trials_df.iterrows():
            if drug['drug'] in trial['scientific_title']:
                mentions.append({'journal': trial['journal'], 'date': trial['date'], 'source': 'Clinical Trial'})

        if mentions:
            graph[drug['drug']] = mentions

    return graph
