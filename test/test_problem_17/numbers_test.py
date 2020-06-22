import unittest
from ddt import ddt, data, unpack

from problem_17.solution.numbers import get_number_name

@ddt
class TestNumber(unittest.TestCase):

    @data(
        [1, "one"], 
        [2, "two"], 
        [3, "three"],
        [4, "four"],
        [5, "five"], 
        [6, "six"],
        [7, "seven"],
        [8, "eight"],
        [9, "nine"]
    )
    @unpack
    def test_single_digits(self, number, name):
        self.assertEqual(get_number_name(number), name)

    @data(
        [10, "ten"],
        [11, "eleven"], 
        [12, "twelve"], 
        [13, "thirteen"],
        [14, "fourteen"],
        [15, "fifteen"], 
        [16, "sixteen"],
        [17, "seventeen"],
        [18, "eighteen"],
        [19, "nineteen"]
    )
    @unpack
    def test_double_digits_less_than_twenty(self, number, name):
        self.assertEqual(get_number_name(number), name)

    @data(
        [20, "twenty"],
        [30, "thirty"],
        [40, "forty"],
        [50, "fifty"],
        [60, "sixty"],
        [70, "seventy"],
        [80, "eighty"],
        [90, "ninety"]
    )
    @unpack
    def test_double_digit_multiples_of_ten(self, number, name):
        self.assertEqual(get_number_name(number), name)

    def test_twenty_on(self):
        self.assertEqual(get_number_name(21), "twenty-one")

    @data(
        [100, "one hundred"],
        [200, "two hundred"],
        [300, "three hundred"],
        [400, "four hundred"],
        [500, "five hundred"],
        [600, "six hundred"],
        [700, "seven hundred"],
        [800, "eight hundred"],
        [900, "nine hundred"]
    )
    @unpack
    def test_hundreds(self, number, name):
        self.assertEqual(get_number_name(number), name)

    def test_one_hundred_and_one(self):
        self.assertEqual(get_number_name(101), "one hundred and one")

    def test_three_hundred_and_forty_two(self):
        self.assertEqual(get_number_name(342), "three hundred and forty-two")

    def test_one_thousand(self):
        self.assertEqual(get_number_name(1000), "one thousand")
