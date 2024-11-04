from src.data_pipeline import build_pipeline

def test_build_pipeline():
    drugs_df, pubmed_df, clinical_trials_df = build_pipeline()
    assert not drugs_df.empty, "drugs_df ne doit pas être vide"
    assert not pubmed_df.empty, "pubmed_df ne doit pas être vide"
    assert not clinical_trials_df.empty, "clinical_trials_df ne doit pas être vide"
