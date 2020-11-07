from .. import exceptions as core_exceptions
from .. import interfaces as core_interfaces
from . import unittests


import sys


class MachineLearning(core_interfaces.AnalyzerStrategy):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:
        return []


if __name__ == "__main__":

    ml = MachineLearning()
    print("MachineLearning")

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        quit(unittests.test(ml))

