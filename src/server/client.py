import asyncio
import websockets

from .server import WebSocket

class Client:

    def __init__(self, addr="localhost", port=8000):
        self.sock = WebSocket(addr, port)
        self.requests = []
        self.conn_uri = 'ws://' + addr + ":" + str(port)

    async def sendRequest(self):
        async with websockets.connect(self.conn_uri) as so:
            for i in range(1, 100, 1):
                await self.sock.y.send("[Client][Sent]: Hewwo")
#                 # data_rcv = await self.sock.y.recv(); 
#                 # print("data received from server : " + data_rcv)
                
    def executeSend(self):
        asyncio.get_event_loop().run_until_complete(self.sendRequest())

if __name__ == "__main__":
    print("Client")
    c = Client()
    c.executeSend()
