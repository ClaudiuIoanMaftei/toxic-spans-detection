import pytest
import asyncio
import websockets

from src.server.client import Client
from src.server import Server

### Client ###

class TestClient():

    cl = Client()

    def test_client_executeSend(self):
        # No connection yet
        assert TestClient.cl.executeSend() == False