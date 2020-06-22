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


