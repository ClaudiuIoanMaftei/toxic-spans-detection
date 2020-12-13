from src.server.core.ml import MachineLearning

import pytest


@pytest.fixture()
def machine_learning():
    return MachineLearning()

def test_1(machine_learning):
    assert machine_learning.analyze("") == []

def test_2(machine_learning):
    assert machine_learning.analyze("Hello friend") == []

def test_3(machine_learning):
    assert machine_learning.analyze("Have a nice day") == []

def test_4(machine_learning):
    assert machine_learning.analyze("You are such an idiot") == [16, 17, 18, 19, 20]

def test_5(machine_learning):
    assert machine_learning.analyze("This man is a sickening, mentally ill joke.") == [38, 39, 40, 41]
