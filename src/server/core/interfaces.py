from ..preprocessing import preproc


class AnalyzerStrategy:
    def analyze(self, preprocessed) -> [int]:
        """
        Main method for analyzing components
        :param preprocessed: normalized input string
        :return: array of integers representing toxic spans indexes
        """
        pass