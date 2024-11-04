import pandas as pd
from src.data_loader import load_csv, load_json, standardize_date_format

def test_load_csv():
    df = load_csv('data/drugs.csv')
    assert isinstance(df, pd.DataFrame), "La sortie doit être un DataFrame"
    assert not df.empty, "Le DataFrame ne doit pas être vide"

def test_load_json():
    df = load_json('data/pubmed.json')
    assert isinstance(df, pd.DataFrame), "La sortie doit être un DataFrame"
    assert not df.empty, "Le DataFrame ne doit pas être vide"

def test_standardize_date_format():
    data = {'date': ['01/01/2020', '15/02/2020']}
    df = pd.DataFrame(data)
    df = standardize_date_format(df, 'date', current_format='%d/%m/%Y', target_format='%Y-%m-%d')
    assert df['date'].iloc[0] == '2020-01-01', "La date doit être formatée en 'YYYY-MM-DD'"
    assert df['date'].iloc[1] == '2020-02-15', "La date doit être formatée en 'YYYY-MM-DD'"
