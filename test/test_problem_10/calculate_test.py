import pytest

from src.problem_10.solution.calculate import get_sum_of_primes_less_than_n

class TestGetSumOfPrimesLessThanN:
    def test_sum_of_primes_less_than_2(self):
        value = get_sum_of_primes_less_than_n(2)
        assert value == 0

    def test_sum_of_primes_less_than_3(self):
        value = get_sum_of_primes_less_than_n(3)
        assert value == 2
    
    def test_sum_of_primes_less_than_4(self):
        value = get_sum_of_primes_less_than_n(4)
        assert value == 5
    
    def test_sum_of_primes_less_than_10(self):
        value = get_sum_of_primes_less_than_n(10)
        assert value == 17
