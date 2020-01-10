import pytest

from problem_7.solution.prime import is_prime_number

class TestPrime:
    def test_even_numbers_greater_than_2_are_not_prime(self):
        assert is_prime_number(2) == True
        assert is_prime_number(4) == False
        assert is_prime_number(6) == False
        assert is_prime_number(8) == False