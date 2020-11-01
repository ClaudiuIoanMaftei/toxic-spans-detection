"""
Module - ProcessHandler - Handles process queue.
"""
from .core import core
from .preprocessing import preproc
from .postprocessing import postproc
from . import interfaces as server_interfaces

class SyncQueue(server_interfaces.Queue):
    
    self __init__(self):
        self.queue = [] # Stores received requests

    def push(self):
        pass
    def pop(self):
        pass

class ThreadedWorker(server_interfaces.WorkerInterface):
    # The actual execution logic
    def __init__(self, thread_no):
        self.thread_no = thread_no
    
    def initialize(self):
        pass
    def execute(self):
        # Sends input further for preproc, detections...
        pass

class MetricsManager(self):
    # Generates metrics
    def __init__(self):
        pass

    def newMetrics(self):
        pass
    def writeMetrics(self, metrics):
        pass

class RequestManager:
    # Handles the processing queue
    def __init__(self):
        self.requests_queue = SyncQueue()

        self.core = core.Core()
        self.preproc = preproc.Preprocessor()
        self.postproc = postproc.Postprocessor()

    def launch(self):
        pass
    def newRequest(self):
        pass
    def queueSize(self):
        pass