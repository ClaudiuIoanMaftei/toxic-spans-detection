from .server import WebSocket

class Client:

    def __init__(self):
        self.sock = WebSocket()
        self.requests = []

    def sendRequest(self):
        pass

if __name__ == "__main__":
    print("Client")