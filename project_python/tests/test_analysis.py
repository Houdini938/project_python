from src.analysis import journal_with_most_drugs, drugs_mentioned_within_same_journal

def test_journal_with_most_drugs():
    graph = {
        'Aspirin': [{'journal': 'Pain Journal'}, {'journal': 'Pain Journal'}],
        'Ibuprofen': [{'journal': 'Pain Journal'}, {'journal': 'Health Journal'}]
    }
    assert journal_with_most_drugs(graph) == 'Pain Journal', "Le journal avec le plus de mentions de médicaments doit être 'Pain Journal'"

def test_drugs_mentioned_within_same_journal():
    graph = {
        'Aspirin': [{'journal': 'Pain Journal', 'source': 'PubMed'}],
        'Ibuprofen': [{'journal': 'Pain Journal', 'source': 'PubMed'}],
        'Paracetamol': [{'journal': 'Health Journal', 'source': 'PubMed'}]
    }
    result = drugs_mentioned_within_same_journal(graph, 'Aspirin')
    assert 'Ibuprofen' in result, "Ibuprofen doit être mentionné dans le même journal que Aspirin"
    assert 'Paracetamol' not in result, "Paracetamol ne doit pas être mentionné dans le même journal que Aspirin"
