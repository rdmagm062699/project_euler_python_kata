import pytest

from problem_6.solution.calculate import get_sum_of_squares, get_square_of_sum

class TestCalculate:
    def test_get_sum_of_squares_for_max_of_10(self):
        value = get_sum_of_squares(max_number=10)
        assert value == 385, 'got {}'.format(value)

    def test_get_square_of_sum_for_max_of_10(self):
        value = get_square_of_sum(max_number=10)
        assert value == 2640 , 'got {}'.format(value)
