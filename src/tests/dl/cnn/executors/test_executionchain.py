import pytest

from src.server.core.dl.cnn.executors.networkhandler import NetworkHandler


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


class TestNetworkHandler(NetworkHandler):

    def __init__(self):
        super().__init__()

    def init(self, **kwargs):
        pass


def test_add_methods():
    executor = TestNetworkHandler()
    executor.init()