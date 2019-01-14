import pytest

from problem_5.solution.calculate import get_smallest_number_divisible_by_range

class TestCalculate:
    def test_smallest_number_divisible_by_1_to_5(self):
        value = get_smallest_number_divisible_by_range(max_divisor=5)
        assert value == 60
