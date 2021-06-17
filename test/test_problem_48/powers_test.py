import unittest

from problem_48.solution.powers import get_power_sequence_sum


class TestPowers(unittest.TestCase):

    def test_range_of_1_returns_1(self):
        self.assertEqual(get_power_sequence_sum(1, 1), 1)

    def test_range_of_1_to_2_returns_5(self):
        self.assertEqual(get_power_sequence_sum(1, 2), 5)

    def test_range_of_1_to_3_returns_14(self):
        self.assertEqual(get_power_sequence_sum(1, 3), 32)
