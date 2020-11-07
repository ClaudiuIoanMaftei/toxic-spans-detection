from .cnn.executors import default_execution as DefaultExecution
from .. import exceptions as core_exceptions
from .. import interfaces as core_interfaces


class DeepLearning(core_interfaces.AnalyzerStrategy):
    _execution_strategy = None

    def __init__(self):
        self._execution_strategy = DefaultExecution()
        self._train("")

    def analyze(self, preprocessed) -> [int]:
        return self._execution_strategy.execute()

    def _train(self, input_directory):
        """
        Trains the CNN with the given input files
        :param input_directory: directory with one or more CSV files used as input data
        :return: None
        """
        pass


if __name__ == "__main__":
    print("DeepLearning")
