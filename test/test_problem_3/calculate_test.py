import pytest

from problem_3.solution.calculate import get_highest_prime

class TestCalculate:

    def test_get_higest_prime(self):
        value = get_highest_prime(13195)
        assert value == 29, 'got {}'.format(value)
