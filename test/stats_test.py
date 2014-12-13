import unittest
from math import sqrt
from src.stats import Statistics

class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.stats = Statistics()

    def populate(self, data):
        self.stats.update(data)

    def tearDown(self):
        del self.stats
    
    def test_empty_sum(self):
        self.assertEqual(self.stats.sum, 0.0)

    def test_zero_sum(self):
        self.populate(0)
        self.assertEqual(self.stats.sum, 0.0)

    def test_single_sum(self):
        self.populate(1)
        self.assertEqual(self.stats.sum, 1.0)

    def test_double_sum(self):
        self.populate([1,2])
        self.assertEqual(self.stats.sum, 3.0)

    def test_triple_sum(self):
        self.populate([1,2,3])
        self.assertEqual(self.stats.sum, 6.0)

    def test_many_values_sum(self):
        self.populate([1,2,3,4,5,6,7,8,9,10,123,789, 1234567890])
        self.assertEqual(self.stats.sum, 1234568857)
    
    def test_multiple_value_sum(self):
        exp = 0.0
        for x in range(1000):
            with self.subTest(x=x):
                exp += x
                self.populate(x)
                self.assertEqual(self.stats.sum, exp)

    def test_empty_n(self):
        self.assertEqual(self.stats.n, 0)

    def test_single_n(self):
        self.populate(range(1))
        self.assertEqual(self.stats.n, 1)
    
    def test_two_n(self):
        self.populate(range(2))
        self.assertEqual(self.stats.n, 2)

    def test_three_n(self):
        self.populate(range(3))
        self.assertEqual(self.stats.n, 3)

    def test_multiple_n(self):
        self.populate(range(1234))
        self.assertEqual(self.stats.n, 1234)

    def test_empty_mean(self):
        self.assertEqual(self.stats.mean, 0.0)

    def test_single_mean(self):
        self.populate(7)
        self.assertEqual(self.stats.mean, 7.0)

    def test_two_mean_same(self):
        self.populate([7, 7])
        self.assertEqual(self.stats.mean, 7.0)

    def test_three_mean_same(self):
        self.populate([7, 7, 7])
        self.assertEqual(self.stats.mean, 7.0)

    def test_many_mean_same(self):
        self.populate([7] * 77)
        self.assertEqual(self.stats.mean, 7.0)
    
    def test_two_mean_diff(self):
        self.populate([3, 7])
        self.assertEqual(self.stats.mean, (3 + 7) / 2.0)

    def test_three_mean_diff(self):
        self.populate([0, 3, 7])
        self.assertEqual(self.stats.mean, (0 + 3 + 7) / 3.0)

    def test_four_mean_diff(self):
        self.populate([0, 3, 7, 145])
        self.assertEqual(self.stats.mean, (0 + 3 + 7 + 145) / 4.0)
    
    def test_many_values_mean(self):
        exp = 0.0
        for n, x in enumerate(range(3, 3000, 7), start=1):
            with self.subTest(x=x):
                exp = (exp * (n - 1) + x) / n
                self.populate(x)
                self.assertEqual(self.stats.mean, exp)
    
    def test_empty_median(self):
        self.assertRaises(IndexError, lambda : self.stats.median)
    
    def test_single_median(self):
        self.populate(5)
        self.assertEqual(self.stats.median, 5)

    def test_two_median(self):
        self.populate([4, 5])
        self.assertEqual(self.stats.median, (4 + 5) / 2)
    
    def test_three_median(self):
        self.populate([4, 5, 6])
        self.assertEqual(self.stats.median, 5)

    def test_four_median(self):
        self.populate([4, 5, 6, 7])
        self.assertEqual(self.stats.median, (5 + 6) / 2)

    def test_many_median_even(self):
        self.populate(range(1000))
        self.assertEqual(self.stats.median, (1000 - 1) / 2)

    def test_many_median_odd(self):
        self.populate(range(1001))
        self.assertEqual(self.stats.median, int(1001 / 2))

    def test_many_media_unordered(self):
        self.populate([7, 8, 4, 123, 9001, 0, -1, -2, -3, 5, 6, 9, 88, -2, 0])
        self.assertEqual(self.stats.median, 5.0)

    def test_empty_std_dev(self):
        self.assertEqual(self.stats.std_dev, 0.0)
    
    def test_single_std_dev(self):
        self.populate(6)
        self.assertEqual(self.stats.std_dev, 0.0)

    def test_two_std_dev(self):
        self.populate([5, 6])
        self.assertEqual(self.stats.std_dev, sqrt(1/2))

    def test_three_std_dev(self):
        self.populate([5, 6, 7])
        self.assertEqual(self.stats.std_dev, 1.0)

    def test_four_std_dev(self):
        self.populate([5, 6, 7, 8])
        self.assertEqual(self.stats.std_dev, sqrt(5 / 3))

    def test_multiple_std_dev(self):
        self.populate([-5, -2, 0, 1, 5, 6, 7, 8, 19, 30, 43, 89, 112, 772])
        self.assertAlmostEqual(self.stats.std_dev, 202.99214, places=5)

    def test_multiple_std_dev_unordered(self):
        self.populate([6, 8, 1, 3, -17, 18, 32, -49, 7, 14, 21, 0, 3, -5, -9])
        self.assertAlmostEqual(self.stats.std_dev, 18.66318, places=5)

if __name__ == "__main__":
    unittest.main()
