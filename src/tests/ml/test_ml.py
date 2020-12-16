from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect

import pytest

@pytest.fixture()
def machine_learning():
    aspect = AnalyzerAspect()
    ml = MachineLearning()

    aspect.apply(ml)
    return ml

def test_1(machine_learning):
    assert machine_learning.analyze("") == []

def test_2(machine_learning):
    assert machine_learning.analyze("Hello friend") == []

def test_3(machine_learning):
    assert machine_learning.analyze("Have a nice day") == []

def test_4(machine_learning):
    assert machine_learning.analyze("You are stupid") == [8, 9, 10, 11, 12, 13]

def test_5(machine_learning):
    assert machine_learning.analyze("You are such an idiot") == [16, 17, 18, 19, 20]
