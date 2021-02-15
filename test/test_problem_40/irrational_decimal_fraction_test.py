import unittest

from problem_40.solution.irrational_decimal_fraction import IrrationalDecimalFraction


class TestIrrationalDecimalFraction(unittest.TestCase):

    def test_length_of_zero_is_an_empty_list(self):
        expected = ''
        self.assertEqual(IrrationalDecimalFraction(0).value, expected)

    def test_length_of_one(self):
        expected = '1'
        self.assertEqual(IrrationalDecimalFraction(1).value, expected)

    def test_length_of_two(self):
        expected = '12'
        self.assertEqual(IrrationalDecimalFraction(2).value, expected)
