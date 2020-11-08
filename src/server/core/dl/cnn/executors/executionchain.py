import time

from src.server.core.exceptions import UninitializedException

class ExecutionChain:
    """
    Abstract class for defining an execution chain inside the network. This will act like a workflow that
    that passes the input through a number of layers, adjusting parameters as it goes.
    Starting with the entry point and it's arguments, the result will be passed through the execution workflow,
    forwarding the result from one layer to another
    """

    """
    Entry point handler
    """
    _entry_point = None

    """
    Execution chain, a tuple array containing the handler and all the needed metadata to execute it
    """
    _chain = []

    """
    Output filter to parse the chain execution result
    """
    _output_filter = None

    """
    Member used to record the last execution, with whatever data is needed
    """
    _last_execution_metrics = None

    def __init__(self):
        pass

    def entry_point(self, handler, args):
        """
        Define the layer entry point. This is the first handler in the layer.
        :param handler: handler to execute
        :param args: handler specific arguments
        :return:
        """
        self._entry_point = (handler, args)

    def add_layer(self, handler, repetitions=1, forward_result=True, args=None):
        """
        Adds a new layer to the execution stack. This method should be called only after the entry point has been
         defined.
        :param handler: handler to execute
        :param repetitions: number of times the handler will be executed
        :param forward_result: when the handler executes multiple times, specify whether the second and next executions
                               will use the result from the previous execution, or the input for the layer
        :param args: arguments specific for this handler, if custom ones are required. Entry point arguments are used
                     by default
        :return: result from layer execution
        """
        if args is None:
            args = {}
        self._chain.append((handler, repetitions, forward_result, args))

    def output_filter(self, out_filter):
        """
        Sets a final step in the execution chain, used to interpret and normalize the execution result
        :param out_filter: filter to execute
        :return: the normalized output of the execution chain
        """
        self._output_filter = out_filter

    def execute(self):
        """
        Begins the execution with the current layer configuration
        :return: the output of the last layer in the chain if there is no output filter, or it's result otherwise
        """

        if self._entry_point is None:
            raise UninitializedException("No entrypoint defined for the execution chain")

        ep, args = self._entry_point
        self._last_execution_metrics = []

        # Execute the entry point
        start = time.time()
        ep.execute(args)
        self._add_execution_results(ep, 1, args, time.time() - start)

        # Execute the layers chain
        for layer in self._chain:
            handler, repetitions, forward_result, args = layer
            start = time.time()
            for _ in range(repetitions):
                new_args = handler.execute(args)
                if forward_result:
                    args = new_args
            self._add_execution_results(handler, repetitions, args, time.time() - start)

        if self._output_filter is not None:
            return self.output_filter(args)
        else:
            return args

    def get_execution_metrics(self):
        """
        Get the last execution data
        :return: last execution stored information
        """
        return self._last_execution_metrics

    def _add_execution_results(self, handler, times, args, elapsed_time):
        self._last_execution_metrics.append({
            "handler": handler,
            "times": times,
            "args": args,
            "time": str(elapsed_time) + " ms"
        })
