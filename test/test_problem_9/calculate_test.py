import pytest

from src.problem_9.solution.calculate import get_triple_where_sum_is_n

class TestGetTripleWhereSumIsN:
    def test_sum_12(self):
        value = get_triple_where_sum_is_n(12)
        assert value == (3, 4, 5)
