from ..server.core.ml import machinelearning as ml

import pytest

@pytest.fixture()
def machine_learning():
    return ml.MachineLearning()

def test_1(machine_learning):
    assert machine_learning.analyze("Fructuti gura mentei") == []

def test_2(machine_learning):
    assert machine_learning.analyze("Hey pastarnacule") == []