import pytest

from src.server import server

### WebSocket ###

class TestWebSocket():

    ws = server.WebSocket()

    def test_websocket_bind(self):
        assert TestWebSocket.ws.bind() == True

### Server ###

class TestServer():

    sv = server.Server()

    def test_server_start(self):
        assert TestServer.sv.start() == True

    def test_server_run(self):
        assert TestServer.sv.run() == True

    def test_server_shutdown(self):
        assert TestServer.sv.shutdown() == False

    def test_server_handleRequest(self):
        assert TestServer.sv.handleRequest() == True

    def test_server_getRequest(self):
        assert TestServer.sv.getRequest() != ""

    @pytest.mark.parametrize("test_input, expected", [('abc', False)])
    def test_server_verifyRequest(self, test_input, expected):
        assert TestServer.sv.verifyRequest(test_input) == expected

    def test_server_processRequest(self):
        req = ''
        assert TestServer.sv.processRequest(req) == True

### RequestHandler ###

class TestRequestHandler():

    req = ''
    rh = server.RequestHandler(req)

    def test_requesthandler_getCoreResults(self):
        assert TestRequestHandler.rh.getCoreResults() == True

    def test_requesthandler_handle(self):
        assert TestRequestHandler.rh.handle(TestRequestHandler.req) == True