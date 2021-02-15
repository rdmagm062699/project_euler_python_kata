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

    def test_length_of_nine(self):
        expected = '123456789'
        self.assertEqual(IrrationalDecimalFraction(9).value, expected)

    def test_length_of_forty_nine(self):
        expected = '1234567891011121314151617181920212223242526272829'
        self.assertEqual(IrrationalDecimalFraction(49).value, expected)

    def test_length_of_twenty(self):
        expected = '12345678910111213141'
        self.assertEqual(IrrationalDecimalFraction(20).value, expected)
