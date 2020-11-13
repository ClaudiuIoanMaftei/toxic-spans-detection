import pytest
import asyncio
import websockets

from src.server import client
from src.server import server

### Client ###

class TestClient():

    cl = client.Client()

    def test_client_executeSend(self):
        # No connection yet
        assert TestClient.cl.executeSend() == False