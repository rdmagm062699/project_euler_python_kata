import unittest

from problem_20.solution.number import get_sum_of_digits, get_factorial

class TestSumOfDigits(unittest.TestCase):

    def test_one_returns_1(self):
        self.assertEqual(get_sum_of_digits(1), 1)

    def test_eleven_returns_2(self):
        self.assertEqual(get_sum_of_digits(11), 2)

class TestFactorial(unittest.TestCase):

    def test_factorial_of_2_is_2(self):
        self.assertEqual(get_factorial(2), 2)

    def test_factorial_of_3_is_6(self):
        self.assertEqual(get_factorial(3), 6)
