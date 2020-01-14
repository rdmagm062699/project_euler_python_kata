import pytest

from problem_7.solution.calculate import get_nth_prime_number

class TestCalculate:
    def test_1st_prime_number(self):
        value = get_nth_prime_number(1)
        assert value == 2, 'got {}'.format(value)
    
    def test_2nd_prime_number(self):
        value = get_nth_prime_number(2)
        assert value == 3, 'got {}'.format(value)

    def test_3rd_prime_number(self):
        value = get_nth_prime_number(3)
        assert value == 5, 'got {}'.format(value)

    def test_4th_prime_number(self):
        value = get_nth_prime_number(4)
        assert value == 7, 'got {}'.format(value)
