import pytest

from problem_1.calculate import get_sum_of_numbers_divisible_by_three_and_five

class TestCalculate:

    def test_get_sum_for_10(self):
        value = get_sum_of_numbers_divisible_by_three_and_five(10)
        assert value == 23
