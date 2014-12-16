import multiprocessing
from collections import deque
from abc import ABCMeta, abstractmethod

class Runner(metaclass=ABCMeta):
    
    @abstractmethod
    def start(self, func, *args, **kwargs):
        pass

    @abstractmethod
    def results(self):
        pass

class ProcessRunner(Runner):
    
    def __init__(self, *args, **kwargs):
        self._results = kwargs['results'] if 'results' in kwargs else deque()

class SingleprocessRunner(ProcessRunner):
    
    def __init__(self, *args, **kwargs):
        super(SingleprocessRunner, self).__init__(*args, **kwargs)
    
    def start(self, func, *args, **kwargs):
        self._results.append(func(*args, **kwargs))

    def results(self):
        for result in self._results:
            yield result

class MultiprocessRunner(ProcessRunner):
    
    def __init__(self, *args, **kwargs):
        super(MultiprocessRunner, self).__init__(*args, **kwargs)
        procs = kwargs['processors'] if 'processors' in kwargs else multiprocessing.cpu_count()
        self._pool = kwargs['pool'] if 'pool' in kwargs else multiprocessing.Pool(processes=procs)
        self._num_of_results = 0

    def _max_wait(self, n):
        return n > self._num_of_results * 2

    def start(self, func, *args):
        self._num_of_results += 1
        self._results.append(self._pool.apply_async(func, args))

    def results(self):
        counter = 0
        while len(self._results) > 0:
            result = self._results.pop()
            counter += 1
            try:
                yield result.get(0.25)
            except multiprocessing.TimeoutError:
                if self._max_wait(counter): self._terminate()
                else: self._results.appendleft(result)

    def _terminate(self):
       self._pool.close()
       self._pool.terminate()
       self._results.clear()

