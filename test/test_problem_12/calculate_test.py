import pytest

from problem_12.solution.calculate import find_triangular_number_divisible_by_more_than_n_numbers

class TestHighlyDivisibleTriangular:

    def test_first_triangular_divisible_by_more_than_zero_numbers(self):
        triangular = find_triangular_number_divisible_by_more_than_n_numbers(0)
        assert triangular == 1, 'got {}'.format(triangular)

    def test_first_triangular_divisible_by_more_than_one_numbers(self):
        triangular = find_triangular_number_divisible_by_more_than_n_numbers(1)
        assert triangular == 3, 'got {}'.format(triangular)

    def test_first_triangular_divisible_by_more_than_five_numbers(self):
        triangular = find_triangular_number_divisible_by_more_than_n_numbers(5)
        assert triangular == 28, 'got {}'.format(triangular)
