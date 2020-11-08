import pytest

from src.server import client

### Client ###

class TestClient():

    cl = client.Client()

    def test_client_sendRequest(self):
        assert TestClient.cl.sendRequest() == True