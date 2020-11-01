from src.server.core.dl.cnn.executors.executionstrategy import ExecutionStrategy


class DefaultExecution(ExecutionStrategy):
    """
    Implementation for the default execution chain. This is the one described by our reference document:
    https://arxiv.org/pdf/1802.09957.pdf
    """

    def __init__(self):
        super().__init__()

    def init(self, **kwargs):
        pass
