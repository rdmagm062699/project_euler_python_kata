import pytest

from problem_12.solution.calculate import find_triangular_number_divisible_by_more_than_n_numbers

class TestHighlyDivisibleTriangular:

    def test_first_triangular_divisible_by_more_than_zero_numbers(self):
        triangular = find_triangular_number_divisible_by_more_than_n_numbers(0)
        assert triangular == 1, 'got {}'.format(triangular)
