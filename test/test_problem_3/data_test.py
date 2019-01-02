import pytest

from problem_4.solution.data import get_possible_factors

class TestGetPossibleFactors:

    def test_get_one_digit_factors(self):
        factors = get_possible_factors(1)
        expected_factors = list(range(1,10))
        assert factors == expected_factors, 'got {}'.format(factors)
