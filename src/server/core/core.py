from . import exceptions as core_exceptions
from . import interfaces as core_interfaces
from .dl import deeplearning as dl
from .ml import machinelearning as ml
from ..preprocessing import preproc
from ..aop import aop

class Context:

    def __init__(self, strategy: core_interfaces.AnalyzerStrategy) -> None:
        self._strategy = strategy

        #Init aspect
        self.analyzer_aspect = aop.AnalyzerAspect()

    def strategy(self) -> core_interfaces.AnalyzerStrategy:
        return self._strategy

    def analyze(self, preprocessed: preproc.PreprocResults):

        # Apply aspect
        self.analyzer_aspect.apply(self._strategy)

        self._strategy.analyze(preprocessed)

class Core:
    __instance = None

    def get_instance(self):
        if Core.__instance == None:
            Core()
        return Core.__instance

    def __init__(self):
        if Core.__instance != None:
            raise core_exceptions.SingletonException()
        else:
            Core.__instance = self

    def analyze(self, preprocessed):
        context = Context(ml.MachineLearning())
        context.analyze(preprocessed)


if __name__ == "__main__":
    core = Core()
    core.analyze("hello")

    print("Core")
