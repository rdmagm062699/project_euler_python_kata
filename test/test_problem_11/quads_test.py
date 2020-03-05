import pytest

from src.problem_11.solution.quads import get_max_product_of_adjacent

class TestGetMaxProductOfAdjacent:
    def test_list_of_four_numbers_returns_product_of_those_four(self):
        list = [1,1,1,1]
        value = get_max_product_of_adjacent(list)
        assert value == 1
