# import asyncio
#
# import websocket as websocket
# import websockets
#
# from src.server.core import Core
# from src.server.postprocessor import PostProcessor
# from src.server.preprocessor import PreProcessor
#
#
# class WebSocket:
#     def __init__(self, addr = None, port = None):
#         self.addr = addr
#         self.port = port
#         self.x = ''
#
#     def bind(self, action):
#         self.x = websockets.serve(action, self.addr, self.port)
#
#
# class RequestHandler:
#     # Is instantiated by client request
#     def __init__(self, req):
#         self.thread_no = 'current_thread'
#         self.data = req
#         self.core_results = []
#         self.response ='default'
#
#     def getCoreResults(self):
#         self.core_results = ['htfefahfdha', 'dsfsadgadeh']
#         return self.core_results
#
#     def handle(self):
#         """
#         Actual execution logic
#         input -> preproc -> core (dl/ml) -> postproc -> response
#         """
#         self.response = "Final"
#
#
# class Server:
#
#     def __init__(self, addr="127.0.0.1", port=8000, queue_max_size=10):
#
#         self.is_up = False
#         self.queue = []
#         self.sock = WebSocket(addr, port)
#         self.queue_max_size = queue_max_size
#
#         self.core = Core()
#         self.preproc = PreProcessor()
#         self.postproc = PostProcessor()
#
#     def start(self):
#         # Starting up the server
#         print("Starting server")
#         self.is_up = True
#
#     def run(self):
#         # Server is running, applying requests
#         print("Running server")
#         try:
#             self.sock.bind(self.handleRequest)
#             asyncio.get_event_loop().run_until_complete(self.sock.x)
#             print("connection")
#             asyncio.get_event_loop().run_forever()
#             # print(res)
#             return True
#         except:
#             return False
#
#     def shutdown(self):
#         # Server is shutting down
#         self.is_up = False
#
#     async def handleRequest(self):
#         print("A")
#         # Handles requests
#         while self.is_up:
#             received_data = self.getRequest()
#             print("[Server][Received]: " + received_data)
#             if self.verifyRequest(received_data):
#                 self.processRequest(received_data)
#
#     async def getRequest(self):
#         # Getting web client request
#         received_data = await websocket.recv()
#         return received_data
#
#     def verifyRequest(self, req):
#         # Verifies request's validity to proceed further
#         min_size = 5
#         max_size = 500
#         if (len(req) < min_size) or (len(req) > max_size):
#             return False
#         else:
#             return True
#
#     def processRequest(self, req):
#         # Instantiates request handler that processes/executes the request
#         try:
#             req_handler = RequestHandler(req)
#             self.queue.append(req_handler)
#             req_handler.handle()
#             return True
#         except:
#             return False
#
#
# if __name__ == "__main__":
#     print("Server")
#     Server().run()

import asyncio
import websockets
import json

from src.server.core import Core


async def handler(websocket, path):
    # test_text = await websocket.recv()
    # print(test_text)

    core = Core()
    core.analyze("suck")

    ans = [10,11,12,13,14,15,51,52,53,54,55,56]

    await websocket.send(json.dumps(ans))

start_server = websockets.serve(handler, "127.0.0.1", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()