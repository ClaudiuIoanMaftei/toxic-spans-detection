from src.server.preprocessor import PreProcessor

import pytest

@pytest.fixture()
def preproc():
    p=PreProcessor("This is a test about dogs.")
    p.tokenize()
    p.lemmatize()
    p.generate_synonym_dictionary()
    return p.generate_results()

def test_1(result):
    assert "cat" in result.data["synonyms"]["dog"]

def test_2(result):
    assert len(result.data["tokens"])==7

def test_3(result):
    assert len(result.data["tokens"])!=7
