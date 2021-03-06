import pytest

from problem_12.solution.divisors import get_number_of_divisors

class TestGetNumberOfDivisors:

    def test_get_number_of_divisors_for_1(self):
        divisors = get_number_of_divisors(1)
        assert divisors == 1, 'got {}'.format(divisors)

    def test_get_number_of_divisors_for_3(self):
        divisors = get_number_of_divisors(3)
        assert divisors == 2, 'got {}'.format(divisors)

    def test_get_number_of_divisors_for_6(self):
        divisors = get_number_of_divisors(6)
        assert divisors == 4, 'got {}'.format(divisors)

    def test_get_number_of_divisors_for_144(self):
        divisors = get_number_of_divisors(144)
        assert divisors == 15, 'got {}'.format(divisors)
