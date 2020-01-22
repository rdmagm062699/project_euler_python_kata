import pytest

from src.problem_9.solution.problem import get_product_of_triple_where_sum_is_n

class TestProductOfTripleWhereSumIsN:
    def test_sum_30(self):
        value = get_product_of_triple_where_sum_is_n(30)
        assert value == 780
