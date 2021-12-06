from threading import Thread


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        """ Performs the creation of an object of type ThreadWithReturnValue

        :param group: group of thread
        :param target: target of thread
        :param name: name of thread
        :param args: args of thread
        :param kwargs: kwargs of thread
        :param Verbose: Verbose of thread
        """
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = []

    def run(self):
        """ Run the custom thread

        """
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        """ Do the join of thread

        """
        Thread.join(self, *args)
        return self._return
