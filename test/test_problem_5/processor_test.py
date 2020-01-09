import pytest

from problem_5.solution.processor import check_all_divisors, get_divisors_to_check

class TestCheckAllDivisors:
    def test_4_not_evenly_divisible_by_all_numbers_from_1_to_3(self):
        value = check_all_divisors(dividend=4, max_divisor=3)
        assert value == False

    def test_6_is_evenly_divisible_by_all_humbers_from_1_to_3(self):
        value = check_all_divisors(dividend=6, max_divisor=3)
        assert value == True

    def test_12_is_evenly_divisible_by_all_humbers_from_1_to_4(self):
        value = check_all_divisors(dividend=12, max_divisor=4)
        assert value == True

class TestGetDivisorsToCheck:
    def test_2_returns_expected_value(self):
        value = get_divisors_to_check(max_divisor=2)
        assert value == [2]

    def test_2_returns_expected_value(self):
        value = get_divisors_to_check(max_divisor=3)
        value.sort()
        assert value == [2, 3], 'got {}'.format(value)

    def test_4_returns_expected_value(self):
        value = get_divisors_to_check(max_divisor=4)
        value.sort()
        assert value == [3, 4], 'got {}'.format(value)
