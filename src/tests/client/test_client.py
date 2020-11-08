import pytest
import asyncio
import websockets

from src.server import client

### Client ###

class TestClient():

    cl = client.Client()

    def test_client_executeSend(self):
        with pytest.raises(ConnectionRefusedError):
            TestClient.cl.executeSend()