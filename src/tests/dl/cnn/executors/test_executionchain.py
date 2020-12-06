import pytest

from src.server.core.dl.cnn.executors.executionstrategy import ExecutionStrategy


class HandlerMock:
    def __init__(self):
        print("Mock Handler created")

    def execute(self, kwargs):
        print("Executed mock handler with args: " + str(kwargs))
        return kwargs


class OutputFilterMock:
    def __init__(self):
        print("Mock output filter created")

    def execute(self, output):
        print("Output filter called with: " + output)


handler_mock = HandlerMock()
output_filter_mock = OutputFilterMock()

convolutional_args1 = {'kern_x': 5, 'kern_y': 5, 'lf': 3.3, 'w': 4}
convolutional_args2 = {'kern_x': 15, 'kern_y': 15, 'lf': 2.1, 'w': 2}
convolutional_args3 = {'kern_x': 25, 'kern_y': 25, 'lf': 1.1, 'w': 1.1}

polling_args = {'directions': 4, 'scale': 1.5}

fnn_args = {'kern_x': 1, 'kern_y': 1, 'lf': 1.2, 'w': 2}


class TestExecutionStrategy(ExecutionStrategy):

    def __init__(self):
        super().__init__()

    def init(self, **kwargs):
        self._execution_chain.entry_point(handler_mock, convolutional_args1)

        self._execution_chain.add_layer(handler_mock, 2, True, convolutional_args2)
        self._execution_chain.add_layer(handler_mock, 1, True, polling_args)
        self._execution_chain.add_layer(handler_mock, 3, True, convolutional_args3)
        self._execution_chain.add_layer(handler_mock, 3, True, polling_args)

        self._execution_chain.output_filter(output_filter_mock)


def test_add_methods():
    executor = TestExecutionStrategy()
    executor.init()
    executor.execute()

    print("Executed test chain.")
    execution_data = executor.get_execution_data()
    print(execution_data)

    # CNN layers may adjust arguments between repetitions, so we cannot test the arguments
    assert(execution_data[0]["handler"] == handler_mock)
    assert(execution_data[0]["times"] == 1)
    assert("time" in execution_data[0])

    assert (execution_data[1]["handler"] == handler_mock)
    assert (execution_data[1]["times"] == 2)
    assert ("time" in execution_data[1])

    assert (execution_data[2]["handler"] == handler_mock)
    assert (execution_data[2]["times"] == 1)
    assert (execution_data[2]["args"] == polling_args)
    assert ("time" in execution_data[2])

    assert (execution_data[3]["handler"] == handler_mock)
    assert (execution_data[3]["times"] == 3)
    assert ("time" in execution_data[3])

    assert (execution_data[4]["handler"] == handler_mock)
    assert (execution_data[4]["times"] == 3)
    assert (execution_data[4]["args"] == polling_args)
    assert ("time" in execution_data[4])
