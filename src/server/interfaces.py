# Server specific interfaces
class InterceptorInterface:
    # Interface - Will Intercept input messages
    def intercept(self, message: str):
        pass

class ValidatorInterface:
    # Interface - Will validate input messages
    def validate(self):
        pass

class QueueInterface:
    # Interface - Will deal with queue
    def push(self):
        pass
    def pop(self):
        pass

class WorkerInterface:
    # Interface - Worker
    def initialize(self):
        pass
    def execute(self):
        pass