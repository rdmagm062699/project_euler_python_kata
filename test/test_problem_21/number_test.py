import unittest

from problem_21.solution.number import get_proper_divisors

class TestGetProperDivisors(unittest.TestCase):

    def test_only_proper_divisor_of_2_is_1(self):
        self.assertEqual(get_proper_divisors(2), [1])

    def test_one_has_no_proper_divisors(self):
        self.assertEqual(get_proper_divisors(1), [])

    def test_proper_divisors_of_4_are_1_and_2(self):
        self.assertEqual(get_proper_divisors(4), [1, 2])

    def test_proper_divisors_of_100(self):
        self.assertEqual(sorted(get_proper_divisors(100)), [1, 2, 4, 5, 10, 20, 25, 50])
