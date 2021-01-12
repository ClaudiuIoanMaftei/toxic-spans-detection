from src.server.preprocessor import PreProcessor


def test_1():
    preproc = PreProcessor("This is a test about dogs")
    preproc.lower()
    preproc.tokenize()
    preproc.remove_stopwords()
    preproc.lemmatize()
    results = preproc.generate_results()

    assert results.data["tokens"] == ["test", "dogs"]

def test_2():
    preproc = PreProcessor("")
    preproc.lower()
    preproc.tokenize()
    preproc.remove_stopwords()
    preproc.lemmatize()
    results = preproc.generate_results()

    assert results.data["tokens"] == []

def test_3():
    preproc = PreProcessor("Waiting running")
    preproc.lower()
    preproc.tokenize()
    preproc.remove_stopwords()
    preproc.lemmatize()
    results = preproc.generate_results()

    assert results.data["lemmas"] == ["wait", "run"]


