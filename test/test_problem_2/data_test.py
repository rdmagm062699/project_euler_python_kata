import pytest

from problem_2.solution.data import sum_even_numbers

class TestSumEvenNumbers:

    def test_empty_list_returns_0(self):
        value = sum_even_numbers([])
        assert value == 0, 'got {}'.format(value)

    def test_returns_expected_value_for_populated_list(self):
        value = sum_even_numbers([1,2,4,6,9,10])
        assert value == 22, 'got {}'.format(value)
