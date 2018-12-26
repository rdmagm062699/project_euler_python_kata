import pytest

from problem_2.solution.calculate import get_sum_of_even_numbers_in_fibonacci_sequence

class TestCalculate:

    def test_get_sum_for_evens_in_fibonacci(self):
        value = get_sum_of_even_numbers_in_fibonacci_sequence(35)
        assert value == 44, 'got {}'.format(value)
