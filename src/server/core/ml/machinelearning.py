from .. import exceptions as core_exceptions
from .. import interfaces

class MachineLearning(interfaces.AnalyzerInterface):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:
        pass

if __name__ == "__main__":

    ml = MachineLearning()
    print("MachineLearning")