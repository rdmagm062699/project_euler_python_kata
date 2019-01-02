import pytest

from problem_3.solution.primes import get_primes

class TestGetFibonacciUpTo:

    def test_get_primes_for_2(self):
        primes = get_primes(2)

        assert primes == [2]

    def test_get_primes_for_3(self):
        primes = get_primes(3)

        assert primes == [3]
