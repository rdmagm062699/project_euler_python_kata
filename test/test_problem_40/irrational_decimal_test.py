import unittest

from problem_40.solution.irrational_decimal import get_fraction_digits


class TestIrrationalDecimalFraction(unittest.TestCase):

    def test_length_of_zero_is_an_empty_list(self):
        expected = ''
        self.assertEqual(get_fraction_digits(0), expected)

    def test_length_of_one(self):
        expected = '1'
        self.assertEqual(get_fraction_digits(1), expected)

    def test_length_of_two(self):
        expected = '12'
        self.assertEqual(get_fraction_digits(2), expected)

    def test_length_of_nine(self):
        expected = '123456789'
        self.assertEqual(get_fraction_digits(9), expected)

    def test_length_of_forty_nine(self):
        expected = '1234567891011121314151617181920212223242526272829'
        self.assertEqual(get_fraction_digits(49), expected)

    def test_length_of_twenty(self):
        expected = '12345678910111213141'
        self.assertEqual(get_fraction_digits(20), expected)
