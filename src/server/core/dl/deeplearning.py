from .. import exceptions as core_exceptions
from .. import interfaces as core_interfaces


class DeepLearning(core_interfaces.AnalyzerStrategy):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:
        pass

    def train(self, input_directory):
        """
        Trains the CNN with the given input files
        :param input_directory: directory with one or more CSV files used as input data
        :return: None
        """
        pass


if __name__ == "__main__":
    print("DeepLearning")
