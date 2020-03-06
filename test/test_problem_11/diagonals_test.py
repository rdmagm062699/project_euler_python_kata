import pytest

from src.problem_11.solution.diagonals import get_max_product_from_all_diagonals

class TestGetMaxProductFromAllDiagonals:
    def test_single_diagonal_top_left_to_bottom_right(self):
        grid = [[1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4]]
        value = get_max_product_from_all_diagonals(grid)
        assert value == 24
