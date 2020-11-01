from .. import exceptions as core_exceptions
from .. import interfaces as core_interfaces

class MachineLearning(core_interfaces.AnalyzerStrategy):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:
        print("MachineLearning: " + preprocessed)

if __name__ == "__main__":

    ml = MachineLearning()
    print("MachineLearning")