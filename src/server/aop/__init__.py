from pytilities import aop
from pytilities.aop import Aspect
from src.server.preprocessor import PreProcessor
import time


class AnalyzerAspect(Aspect):

    def __init__(self):
        Aspect.__init__(self)

        self._advice_mappings["call", "analyze"] = self._advice
        self._advice_mappings["call", "execute"] = self._advice


    def _advice(self):

        # Start time
        start_time = int(round(time.time()*1000))

        # Object, function information
        object = str((yield aop.advised_instance).__class__.__name__)
        function = str((yield aop.advised_attribute)[0])

        # Verifying arguments
        _arguments = (yield aop.arguments)
        _instance = _arguments[0][0]
        _text = _arguments[0][1]

        # Security
        # Cutting strings that are too long
        _text = _text[:1000]

        # Preprocessing Text
        preproc = PreProcessor(_text)

        #Continuing execution with the new arguments
        yield aop.proceed(_instance, preproc)

        # End time
        exectime = str(int(round(time.time()*1000)) - start_time)

        output = object + "." + function + "(): " + exectime + " ms"

        file = open("aop.log", "a")
        file.write(output + "\n")
        file.close()

        print(output)
