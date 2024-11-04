def clean_data(df):
    df = df.dropna(subset=['title', 'journal', 'date'])
    df['title'] = df['title'].str.upper()
    return df
