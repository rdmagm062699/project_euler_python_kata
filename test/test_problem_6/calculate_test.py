import pytest

from problem_6.solution.calculate import get_sum_of_squares

class TestCalculate:
    def test_get_sum_of_squares_for_max_of_10(self):
        value = get_sum_of_squares(max_number=10)
        assert value == 385, 'got {}'.format(value)
