import pandas as pd
from src.data_cleaning import clean_data

def test_clean_data():
    data = {
        'title': ['Title 1', None, 'Title 3'],
        'journal': ['Journal 1', 'Journal 2', None],
        'date': ['2020-01-01', '2020-01-02', '2020-01-03']
    }
    df = pd.DataFrame(data)
    df_cleaned = clean_data(df)
    assert len(df_cleaned) == 1, "Le DataFrame nettoyé doit contenir uniquement les lignes valides"
    assert df_cleaned['title'].iloc[0] == 'TITLE 1', "Les titres doivent être en majuscules"
