class ExecutionChain:
    """
    Abstract class for defining an execution chain inside the network. This will act like a workflow that
    that passes the input through a number of layers, adjusting parameters as it goes.
    Starting with the entry point and it's arguments, the result will be passed through the execution workflow,
    forwarding the result from one layer to another
    """

    def __init__(self):
        pass

    def entry_point(self, handler, **args):
        """
        Define the layer entry point. This is the first handler in the layer.
        :param handler: handler to execute
        :param args: handler specific arguments
        :return:
        """
        pass

    def add_layer(self, handler, repetitions=1, forward_result=True, **args):
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
        pass

    def output_filter(self, out_filter):
        """
        Sets a final step in the execution chain, used to interpret and normalize the execution result
        :param out_filter: filter to execute
        :return: the normalized output of the execution chain
        """
        pass

    def execute(self):
        """
        Begins the execution with the current layer configuration
        :return: the output of the last layer in the chain if there is no output filter, or it's result otherwise
        """
        pass
