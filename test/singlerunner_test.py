import unittest
from random import randint

from src.runner import SingleprocessRunner

class SingleprocessRunnerTest(unittest.TestCase):

    def setUp(self):
        self.runner = SingleprocessRunner()
        self.func_call_counter = 0
        self.results = []

    def tearDown(self):
        del self.runner
        del self.func_call_counter
        del self.results

    def test_func(self, *args, **kwargs):
        self.func_call_counter += 1
        value = randint(1, 100)
        self.results.append(value)
        return value

    def start_processes(self, n):
        for x in range(n):
            self.runner.start(self.test_func)
    
    def test_results_match(self):
        for x, y in zip(self.runner.results(), self.results):
            self.assertEqual(x, y)


    def test_single_call(self):
        self.start_processes(1)
        self.assertEqual(self.func_call_counter, 1)

    def test_single_call_results_match(self):
        self.start_processes(1)
        self.test_results_match()

    def test_double_call(self):
        self.start_processes(2)
        self.assertEqual(self.func_call_counter, 2)

    def test_double_call_results_match(self):
        self.start_processes(2)
        self.test_results_match()

    def test_triple_call(self):
        self.start_processes(3)
        self.assertEqual(self.func_call_counter, 3)

    def test_triple_call_results_match(self):
        self.start_processes(3)
        self.test_results_match()

    def test_quadruple_call(self):
        self.start_processes(4)
        self.assertEqual(self.func_call_counter, 4)

    def test_quadruple_call_results_match(self):
        self.start_processes(4)
        self.test_results_match() 

    def test_quintuple_call(self):
        self.start_processes(5)
        self.assertEqual(self.func_call_counter, 5)

    def test_quintuple_call_results_match(self):
        self.start_processes(5)
        self.test_results_match()

    def test_multiple_call(self):
        # 997 is the closest prime to 1000.. because why not
        self.start_processes(997)
        self.assertEqual(self.func_call_counter, 997)

    def test_multiple_call_results_match(self):
        self.start_processes(997)
        self.test_results_match()
