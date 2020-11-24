from src.server.core import AnalyzerStrategy
from src.server.core.dl.cnn.executors.default_execution import DefaultExecution
from src.server.core.dl.parsing.vocabulary import Vocabulary


class DeepLearning(AnalyzerStrategy):
    _execution_strategy = None
    dataset_vocabulary = None

    def __init__(self):
        self._execution_strategy = DefaultExecution()
        # self.dataset_vocabulary = Vocabulary.from_csv("../../../../datasets/tsd_train.csv")
        self._train("")

    def analyze(self, preprocessed) -> [int]:
        return None

    def _train(self, input_directory):
        """
        Trains the CNN with the given input files
        :param input_directory: directory with one or more CSV files used as input data
        :return: None
        """
        pass


if __name__ == "__main__":
    print("Deep Learning")
    dl = DeepLearning()
