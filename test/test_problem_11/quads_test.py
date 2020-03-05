import pytest

from src.problem_11.solution.quads import get_max_product_of_adjacent

class TestGetMaxProductOfAdjacent:
    def test_list_of_four_numbers_returns_product_of_those_four(self):
        list = [1,1,1,1]
        value = get_max_product_of_adjacent(list)
        assert value == 1

    def test_list_of_four_different_numbers_returns_product_of_those_four(self):
        list = [1, 2, 3, 4]
        value = get_max_product_of_adjacent(list)
        assert value == 24

    def test_list_of_five_different_numbers_returns_max_product_of_four_adjacent(self):
        list = [2, 2, 3, 4, 5]
        value = get_max_product_of_adjacent(list)
        assert value == 120
