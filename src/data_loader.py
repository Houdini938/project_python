import pandas as pd
import json
import logging

logging.basicConfig(level=logging.INFO)

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

def load_json(file_path):
    try:
        with open(file_path) as f:
            return pd.json_normalize(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading JSON file {file_path}: {e}")
        return pd.DataFrame()

def standardize_date_format(df, date_column, current_format='%d/%m/%Y', target_format='%Y-%m-%d'):
    df[date_column] = pd.to_datetime(df[date_column], format=current_format, errors='coerce').dt.strftime(target_format)
    return df
