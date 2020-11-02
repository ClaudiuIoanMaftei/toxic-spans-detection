from . import server.WebSocket

class Client:

    def __init__(self):
        self.sock = server.WebSocket()
        self.requests = []

    def sendRequest(self):
        pass