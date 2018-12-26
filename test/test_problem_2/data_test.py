import pytest

from problem_2.solution.data import sum_even_numbers

class TestSumEvenNumbers:

    def test_empty_list_returns_0(self):
        value = sum_even_numbers([])
        assert value == 0, 'got {}'.format(value)
