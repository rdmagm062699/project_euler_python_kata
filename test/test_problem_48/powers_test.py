import unittest

from problem_48.solution.powers import get_power_sequence


class TestPowers(unittest.TestCase):

    def test_range_of_1_returns_1(self):
        self.assertEqual(get_power_sequence(1, 1), 1)
