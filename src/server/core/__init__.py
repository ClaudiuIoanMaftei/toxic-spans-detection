from src.server.aop import AnalyzerAspect
from src.server.core.exceptions import SingletonException, DetectionFailedException, UninitializedException
from src.server.core.interfaces import AnalyzerStrategy
from src.server.core.ml import MachineLearning
from src.server.preprocessor import PreprocResults


class Context:

    def __init__(self, strategy: AnalyzerStrategy) -> None:
        self._strategy = strategy

        # Init aspect
        self.analyzer_aspect = AnalyzerAspect()

    def strategy(self) -> AnalyzerStrategy:
        return self._strategy

    def analyze(self, preprocessed: PreprocResults):
        # Apply aspect
        self.analyzer_aspect.apply(self._strategy)

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
            raise SingletonException()
        else:
            Core.__instance = self

    @staticmethod
    def analyze(preprocessed):
        try:
            context = Context(MachineLearning())
            # context = Context(dl.DeepLearning())

            context.analyze(preprocessed)
        except UninitializedException as e:
            print("Failed to initialize analyzing module: %s" % e)
        except DetectionFailedException as e:
            print("Failed to run detection logic: %s" % e)


if __name__ == "__main__":
    core = Core()
    core.analyze("hello")

    print("Core")
