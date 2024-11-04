from src.data_loader import load_csv, load_json, standardize_date_format
from src.data_cleaning import clean_data

class DataPipeline:
    def __init__(self, config):
        self.config = config
        self.drugs_df = None
        self.pubmed_df = None
        self.clinical_trials_df = None
    
    def load_data(self):
        self.drugs_df = load_csv(self.config['data_paths']['drugs'])
        self.pubmed_df = pd.concat([
            load_csv(self.config['data_paths']['pubmed_csv']),
            load_json(self.config['data_paths']['pubmed_json'])
        ])
        self.clinical_trials_df = load_csv(self.config['data_paths']['clinical_trials'])

    def clean_data(self):
        self.pubmed_df = clean_data(self.pubmed_df)
        self.clinical_trials_df = clean_data(self.clinical_trials_df)

    def standardize_dates(self):
        standardize_date_format(self.pubmed_df, 'date')
        standardize_date_format(self.clinical_trials_df, 'date')

    def run(self):
        self.load_data()
        self.clean_data()
        self.standardize_dates()
        return self.drugs_df, self.pubmed_df, self.clinical_trials_df
