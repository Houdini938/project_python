import pytest
from src.data_loader import load_csv, load_json

def test_load_csv():
    df = load_csv('data/test.csv')  # Assurez-vous d'avoir un fichier test
    assert not df.empty

def test_load_json():
    df = load_json('data/test.json')  # Assurez-vous d'avoir un fichier test
    assert not df.empty
