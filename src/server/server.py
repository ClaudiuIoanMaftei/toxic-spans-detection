from .core import core
from .preprocessing import preproc
from .postprocessing import postproc

class Server:

    def __init__(self, addr="localhost", port=8000):
        self.addr = addr
        self.port = port

        self.core = core.Core()
        self.preproc = preproc.Preprocessor()
        self.postproc = postproc.Postprocessor()
    
    def start(self):
        print("Starting server")

if __name__ == "__main__":
    print("Server")