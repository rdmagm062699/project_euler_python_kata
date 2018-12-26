import pytest

from problem_2.solution.fibonacci import get_fibonacci_up_to

class TestGetFibonacciUpTo:

    def test_returns_empty_list_if_less_than_3(self):
        fibonacci = get_fibonacci_up_to(2)
        assert fibonacci == []

    def test_returns_base_fibonacci_if_3(self):
        fibonacci = get_fibonacci_up_to(3)
        assert fibonacci == [1, 2], 'got {}'.format(fibonacci)

    def test_returns_expected_fibonacci_if_4(self):
        fibonacci = get_fibonacci_up_to(4)
        assert fibonacci == [1, 2, 3], 'got {}'.format(fibonacci)

    def test_returns_expected_fibonacci_if_34(self):
        fibonacci = get_fibonacci_up_to(34)
        assert fibonacci == [1, 2, 3, 5, 8, 13, 21], 'got {}'.format(fibonacci)

    def test_returns_expected_fibonacci_if_35(self):
        fibonacci = get_fibonacci_up_to(35)
        assert fibonacci == [1, 2, 3, 5, 8, 13, 21, 34], 'got {}'.format(fibonacci)
