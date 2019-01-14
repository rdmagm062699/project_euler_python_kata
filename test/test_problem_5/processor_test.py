import pytest

from problem_5.solution.processor import check_all_divisors

class TestCheckAllDivisors:
    def test_4_not_evenly_divisible_by_all_numbers_from_1_to_3(self):
        value = check_all_divisors(dividend=4, max_divisor=3)
        assert value == False
