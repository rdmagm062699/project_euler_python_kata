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

    def test_single_diagonal_top_left_to_bottom_right_and_its_opposite(self):
        grid = [[1, 0, 0, 5],
                [0, 2, 4, 0],
                [0, 3, 3, 0],
                [2, 0, 0, 4]]
        value = get_max_product_from_all_diagonals(grid)
        assert value == 120

    def test_diagonal_that_is_not_the_center_diagonal(self):
        grid = [[1, 2, 0, 0, 0],
                [0, 2, 3, 0, 0],
                [0, 0, 3, 4, 0],
                [0, 0, 0, 4, 5],
                [0, 0, 0, 0, 0]]
        value = get_max_product_from_all_diagonals(grid)
        assert value == 120, 'got {}'.format(value)
