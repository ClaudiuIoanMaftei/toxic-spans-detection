import pytest
import asyncio
import websockets

from src.server import client
from src.server import server

### Client ###

class TestClient():

    cl = client.Client()
    sv = server.Server()

    def test_client_executeSend(self):
        TestClient.sv.start()
        TestClient.sv.run()
        assert TestClient.cl.executeSend() == True