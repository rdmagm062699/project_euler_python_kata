import pytest

from src.problem_10.solution.calculate import get_sum_of_primes_less_than_n

class TestGetSumOfPrimesLessThanN:
    def test_sum_of_primes_less_than_2(self):
        value = get_sum_of_primes_less_than_n(2)
        assert value == 2
