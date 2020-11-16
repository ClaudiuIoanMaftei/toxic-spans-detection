from src.server.preprocessor import PreProcessor

import pytest

@pytest.fixture()
def preproc():
    return PreProcessor()

def test_1(preproc):
    results = preproc.preprocess("This is a test about dogs")
    assert results.data["tokens"] == ["This", "is", "a", "test", "about", "dogs"]

def test_2(preproc):
    results = preproc.preprocess("")
    assert results.data["tokens"] == []

def test_3(preproc):
    results = preproc.preprocess("Waiting running")
    assert results.data["lemmas"] == ["Waiting", "run"]

def test_4(preproc):
    results = preproc.preprocess("Sample Text")
    assert results.text == "Sample Text"


