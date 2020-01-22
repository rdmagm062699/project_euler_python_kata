import pytest

from src.problem_9.solution.calculate import get_triple_where_sum_is_n

class TestGetTripleWhereSumIsN:
    def test_sum_12(self):
        value = get_triple_where_sum_is_n(12)
        assert value == (3, 4, 5)

    def test_sum_12(self):
        value = get_triple_where_sum_is_n(132)
        assert value == (11, 60, 61)

    def test_will_not_go_on_forever_if_no_triple_matches_sum(self):
        value = get_triple_where_sum_is_n(133)
        assert value == None 
