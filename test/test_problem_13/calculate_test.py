import pytest

from problem_13.solution.calculate import get_first_n_digits_of_sum

class TestGetDigitsOfSum:

    def test_sum_of_single_item_array_value_zero_first_1_digit_returns_0(self):
        numbers = [0]
        value = get_first_n_digits_of_sum(numbers, 1)
        assert value == 0, 'got {}'.format(value)