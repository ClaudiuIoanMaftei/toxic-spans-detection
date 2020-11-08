from .executionchain import ExecutionChain
from ....exceptions import DetectionFailedException


class ExecutionStrategy:
    """
    Abstract class for creating, training and adjusting an execution chain.
    """

    def __init__(self):
        self._execution_chain = ExecutionChain()

    def init(self, **kwargs):
        """
        initialize the execution chain
        :param kwargs: arguments used for training/tuning the layers
        :return: None
        """
        raise BaseException("Execution strategy must implement init method")

    def execute(self):
        try:
            self._execution_chain.execute()
        except Exception as e:  # Use internal DL exceptions when ready
            raise DetectionFailedException(e)

    def get_execution_data(self):
        return self._execution_chain.get_execution_metrics()
