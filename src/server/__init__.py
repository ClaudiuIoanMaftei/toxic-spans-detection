from src.server.postprocessor import PostProcessor
from src.server.preprocessor import PreProcessor


class WebSocket:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

    def bind(self):
        pass


class RequestHandler:
    # Is instantiated by client request
    def __init__(self, req):
        self.thread_no = 'current_thread'
        self.data = 'getting_data_from_request'
        self.core_results = []
        self.response = 'response'

    def handle(self):
        """
        Actual execution logic
        input -> preproc -> core (dl/ml) -> postproc -> response
        """
        pass


class Server:

    def __init__(self, addr="localhost", port=8000, queue_max_size=10):

        self.is_up = False
        self.queue = []
        self.sock = WebSocket(addr, port)
        self.queue_max_size = queue_max_size

        self.core = core.Core()
        self.preproc = PreProcessor()
        self.postproc = PostProcessor()

    def start(self):
        # Starting up the server
        print("Starting server")
        self.is_up = True
        self.sock.bind()

    def run(self):
        # Server is running, applying requests
        while self.is_up:
            self.handleRequest()

    def shutdown(self):
        # Server is shutting down
        self.is_up = False

    def handleRequest():
        # Handles requests
        req = self.getRequest()
        if self.verifyRequest(req):
            self.processRequest(req)

    def getRequest(self):
        # Getting web client request
        request = 'bla'
        return request

    def verifyRequest(self, req):
        # Verifies request's validity to proceed further
        pass

    def processRequest(self, req):
        # Instantiates request handler that processes/executes the request
        req_handler = RequestHandler(req)
        self.queue.append(req_handler)
        req_handler.handle()


if __name__ == "__main__":
    print("Server")
