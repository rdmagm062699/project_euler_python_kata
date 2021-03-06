import pytest

from problem_12.solution.primes import get_primes

class TestGetFibonacciUpTo:

    def test_get_primes_for_2(self):
        primes = get_primes(2)

        assert primes == [2], 'got {}'.format(primes)

    def test_get_primes_for_3(self):
        primes = get_primes(3)

        assert primes == [3], 'got {}'.format(primes)
        
    def test_get_primes_for_4(self):
        primes = get_primes(4)

        assert primes == [2, 2], 'got {}'.format(primes)
        
    def test_get_primes_for_6(self):
        primes = get_primes(6)

        assert primes == [2, 3], 'got {}'.format(primes)

    def test_get_primes_for_28(self):
        primes = get_primes(28)

        assert primes == [2, 2, 7], 'got {}'.format(primes)
