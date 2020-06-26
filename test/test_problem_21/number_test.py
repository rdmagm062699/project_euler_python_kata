import unittest

from problem_21.solution.number import get_proper_divisors

class TestGetProperDivisors(unittest.TestCase):

    def test_only_proper_divisor_of_2_is_1(self):
        self.assertEqual(get_proper_divisors(2), [1])
