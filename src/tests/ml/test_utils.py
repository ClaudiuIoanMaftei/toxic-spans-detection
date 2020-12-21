from src.server.core.ml.utils import parse_data, spans_to_words

def test_1():
    text  = "Hello, what are you doing?"
    spans = [0, 1, 2, 3, 4, 12, 13, 14]
    assert spans_to_words(spans, text) == ["Hello", "are"]

def test_2():
    object = parse_data("tsd_train.csv")
    assert object[2][0] == [0, 1, 2, 3]