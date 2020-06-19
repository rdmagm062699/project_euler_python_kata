import pytest

from src.problem_11.solution.calculate import get_max_product_from_adjacent_quads

class TestGetMaxProductFromAdjacentQuads:
    def test_row_is_max_produc(self):
        grid = [[3, 3, 3, 3],
                [1, 2, 0, 0],
                [1, 0, 2, 0],
                [1, 0, 0, 2]]
        value = get_max_product_from_adjacent_quads(grid)
        assert value == 81, 'got {}'.format(value)

    def test_colulmn_is_max_produc(self):
        grid = [[9, 3, 3, 3],
                [9, 2, 0, 0],
                [9, 0, 2, 0],
                [9, 0, 0, 2]]
        value = get_max_product_from_adjacent_quads(grid)
        assert value == 6561, 'got {}'.format(value)
