from . import exceptions as core_exceptions
from . import interfaces as core_interfaces
from .dl import deeplearning as dl
from .ml import machinelearning as ml
from ..preprocessing import preproc


class Context:

    def __init__(self, strategy: core_interfaces.AnalyzerStrategy) -> None:
        self._strategy = strategy

    def strategy(self) -> core_interfaces.AnalyzerStrategy:
        return self._strategy

    def analyze(self, preprocessed: preproc.PreprocResults):
        self._strategy.analyze(preprocessed)


class Core:
    __instance = None

    @staticmethod
    def get_instance():
        if Core.__instance is None:
            Core()
        return Core.__instance

    def __init__(self):
        if Core.__instance is not None:
            raise core_exceptions.SingletonException()
        else:
            Core.__instance = self

    @staticmethod
    def analyze(preprocessed):
        try:
            context = Context(ml.MachineLearning())
            # context = Context(dl.DeepLearning())

            context.analyze(preprocessed)
        except core_exceptions.UninitializedException as e:
            print("Failed to initialize analyzing module: %s" % e)
        except core_exceptions.DetectionFailedException as e:
            print("Failed to run detection logic: %s" % e)


if __name__ == "__main__":
    core = Core()
    core.analyze("hello")

    print("Core")
