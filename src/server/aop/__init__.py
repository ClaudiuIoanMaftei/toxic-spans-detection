from pytilities import aop
from pytilities.aop import Aspect
import time


class AnalyzerAspect(Aspect):

    def __init__(self):
        Aspect.__init__(self)

        self._advice_mappings['call', 'analyze', 'execute'] = self._advice

    def _advice(self):
        start_time = int(round(time.time()*1000))

        object = str((yield aop.advised_instance).__class__.__name__)
        function = str((yield aop.advised_attribute)[0])

        exectime = str(int(round(time.time()*1000)) - start_time)
        print(object + "." + function + "(): " + exectime + " ms")

