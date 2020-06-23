import unittest

from problem_16.solution.number import get_sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_one_return_1(self):
        self.assertEqual(get_sum_of_digits(1), 1)