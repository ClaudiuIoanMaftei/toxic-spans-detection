"""
Module - CommunicationManager - Port binding.
Receives messages, validates them sends them further to ProcessHandler.
"""
from . import interfaces as server_interfaces
from . import process_handler as proc_handler

class MessageValidator(server_interfaces.ValidatorInterface):
    # Validates input message - syntactic validation
    def __init__(self):
        pass
    def validate(self, message):
        pass

class MessageInterceptor(server_interfaces.InterceptorInterface):
    # Receives input message and applies additional logic
    def __init__(self):
        pass
    def intercept(self, message):
        pass

class ConnectionManager:

    def __init__(self, addr="localhost", port=8000):
        
        self.addr = addr
        self.port = port

        self.validators_chain = []
        self.interceptors_chain = []

        self.req_manager = proc_handler.RequestManager()

    def start(self):
        # Starting up connection manager
        print("Starting connection manager")

    def getWebRequest(self):
        self.process(input)
        # ...

    def process(self, input):
        # Set up interceptor, validator; push to chains
        pass

    def applyInterceptors(self):
        # Applies interceptors in the same order they were registered
        pass