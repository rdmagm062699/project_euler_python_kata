import unittest

from problem_20.solution.calculate import get_sum_of_digits_of_a_factorial

class TestSumOfFactorialDigits(unittest.TestCase):

    def test_sum_of_factorial_of_10_returns_27(self):
        self.assertEqual(get_sum_of_digits_of_a_factorial(10), 27)
