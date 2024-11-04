import yaml
import json
from src.pipeline import DataPipeline
from src.graph_builder import build_graph
from src.analysis import journal_with_most_drugs, drugs_mentioned_within_same_journal

def load_config():
    with open('config/config.yaml') as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    pipeline = DataPipeline(config)
    drugs_df, pubmed_df, clinical_trials_df = pipeline.run()
    graph = build_graph(drugs_df, pubmed_df, clinical_trials_df)
    
    with open(config['output_path'], 'w') as f:
        json.dump(graph, f, indent=2)
    
    print("Journal with the most drug mentions:", journal_with_most_drugs(graph))
    print("Drugs mentioned with Diphenhydramine:", drugs_mentioned_within_same_journal(graph, 'DIPHENHYDRAMINE'))

if __name__ == "__main__":
    main()
