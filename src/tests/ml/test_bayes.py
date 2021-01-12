from src.server.core.ml.bayes import Bayes, BayesBank

import pytest

@pytest.fixture()
def bayes():
    bayes = Bayes()

    bayes.train(["feature1"], "category1")
    bayes.train(["feature1", "feature2"], "category2")

    return bayes

@pytest.fixture()
def bayes_bank():
    bb = BayesBank()

    bb.train("word1", ["feature1"], "category1")
    bb.train("word2", ["feature1", "feature2"], "category1")

    return bb

def test_1(bayes):
    assert list(bayes.categories.keys()) == ["category1", "category2"]

def test_2(bayes):
    assert bayes.categories["category2"]["count"] == 1
    assert bayes.categories["category1"]["count"] == 1

def test_3(bayes):
    assert bayes.categories["category1"]["features"]["feature1"] == 1
    assert bayes.categories["category2"]["features"]["feature1"] == 1
    assert bayes.categories["category2"]["features"]["feature2"] == 1

def test_5(bayes_bank):
    assert list(bayes_bank.classifiers.keys()) == ["word1", "word2"]
