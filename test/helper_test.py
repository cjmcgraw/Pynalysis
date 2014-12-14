import unittest

from src.helper import pairwise

class HelperFuncTests(unittest.TestCase):

    def test_empty_list_pairwise(self):
        self.assertEqual(list(pairwise([])), [])

    def test_single_value_list_pairwise(self):
        self.assertEqual(list(pairwise([1])), [])

    def test_two_values_list_pairwise(self):
        self.assertEqual(list(pairwise([1,2])), [(1,2),])

    def test_three_values_list_pairwise(self):
        self.assertEqual(list(pairwise([1,2,3])), [(1,2), (2,3)])

    def test_four_values_list_pairwise(self):
        self.assertEqual(list(pairwise([1,2,3,4])), [(1,2), (2,3), (3,4)])

    def test_five_values_list_pairwise(self):
        self.assertEqual(list(pairwise([1,2,3,4,5])), [(1,2), (2,3), (3,4), (4,5)])
