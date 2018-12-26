import pytest

from problem_2.solution.fibonacci import get_fibonacci_up_to

class TestGetFibonacciUpTo:

    def test_returns_empty_list_if_less_than_3(self):
        fibonacci = get_fibonacci_up_to(2)
        assert fibonacci == []

    def test_returns_base_fibonacci_if_3(self):
        fibonacci = get_fibonacci_up_to(3)
        assert fibonacci == [1, 2]
