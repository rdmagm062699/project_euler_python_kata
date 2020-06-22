import pytest

from problem_13.solution.calculate import get_first_n_digits_of_sum

class TestGetDigitsOfSum:

    def test_sum_of_single_item_array_value_zero_first_1_digit_returns_0(self):
        numbers = [0]
        value = get_first_n_digits_of_sum(numbers, 1)
        assert value == '0', 'got {}'.format(value)

    def test_sum_of_one_and_nine_first_1_digit_returns_1(self):
        numbers = [1, 9]
        value = get_first_n_digits_of_sum(numbers, 1)
        assert value == '1', 'got {}'.format(value)

    def test_sum_of_eleven_and_twelve_first_2_digits_returns_23(self):
        numbers = [11, 12]
        value = get_first_n_digits_of_sum(numbers, 1)
        assert value == '23', 'got {}'.format(value)

