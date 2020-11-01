from .dl import deeplearning as dl
from .ml import machinelearning as ml
from . import exceptions as core_exceptions

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
        pass

if __name__ == "__main__":

    core = Core()

    print("Core")