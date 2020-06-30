import unittest

from src.problem_21.solution.number import get_proper_divisors, get_sum_of_amicable_numbers_less_than_n

class TestGetProperDivisors(unittest.TestCase):

    def test_only_proper_divisor_of_2_is_1(self):
        self.assertEqual(get_proper_divisors(2), [1])

    def test_one_has_no_proper_divisors(self):
        self.assertEqual(get_proper_divisors(1), [])

    def test_proper_divisors_of_4_are_1_and_2(self):
        self.assertEqual(get_proper_divisors(4), [1, 2])

    def test_proper_divisors_of_100(self):
        self.assertEqual(sorted(get_proper_divisors(100)), [1, 2, 4, 5, 10, 20, 25, 50])

class TestGetSumOfAmicableNumbers(unittest.TestCase):

    def test_sum_of_amicable_numbers_under_1_is_0(self):
        self.assertEqual(get_sum_of_amicable_numbers_less_than_n(1), 0)

    def test_sum_of_amicable_numbers_under_221_is_220(self):
        self.assertEqual(get_sum_of_amicable_numbers_less_than_n(221), 220)

    def test_sum_of_amicable_numbers_under_1500_is_2898(self):
        self.assertEqual(get_sum_of_amicable_numbers_less_than_n(1500), 2898)
