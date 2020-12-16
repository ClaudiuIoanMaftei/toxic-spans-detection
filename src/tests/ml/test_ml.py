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
    assert machine_learning.analyze("You are an idiot") == [11, 12, 13, 14, 15]

