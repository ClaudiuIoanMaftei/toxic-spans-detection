import pytest

from src.server import server

### WebSocket ###

class TestWebSocket():

    ws = server.WebSocket()

    def test_websocket_bind(self):
        TestWebSocket.ws.bind(print())
        assert str(type(TestWebSocket.ws.x)) == "<class 'websockets.server.Serve'>"

### Server ###

class TestServer():

    sv = server.Server()

    def test_server_start(self):
        TestServer.sv.start()
        assert TestServer.sv.is_up == True

    def test_server_run(self):
        assert TestServer.sv.run() == True

    def test_server_shutdown(self):
        TestServer.sv.shutdown()
        assert TestServer.sv.is_up == False

    # def test_server_handleRequest(self):
    #     assert TestServer.sv.handleRequest() == True

    def test_server_getRequest(self):
        assert TestServer.sv.getRequest() != ""

    @pytest.mark.parametrize("test_input, expected", [('abc', False), ('esti urat', True)])
    def test_server_verifyRequest(self, test_input, expected):
        assert TestServer.sv.verifyRequest(test_input) == expected

    def test_server_processRequest(self):
        req = "Un input foarte foarte jignitor"
        assert TestServer.sv.processRequest(req) == True

### RequestHandler ###

class TestRequestHandler():

    req = 'aaaaaaaaaaaaaaaaa'
    rh = server.RequestHandler(req)

    def test_requesthandler_getCoreResults(self):
        assert len(TestRequestHandler.rh.getCoreResults()) != 0

    def test_requesthandler_handle(self):
        TestRequestHandler.rh.handle()
        assert TestRequestHandler.rh.response != 'default'