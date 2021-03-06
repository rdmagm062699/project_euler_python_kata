import pytest

from src.problem_11.solution.colulmns import get_max_product_from_all_columns

class TestGetMaxProductFromAllColumns:
    def test_one_column_returns_product_of_that_column(self):
        grid = [[1],
                [2],
                [3],
                [4]]
        value = get_max_product_from_all_columns(grid)
        assert value == 24

    def test_two_rows_returns_max_product_from_all_rows(self):
        grid = [[1, 2],
                [2, 3],
                [3, 4],
                [4, 5], 
                [5, 6]]
        value = get_max_product_from_all_columns(grid)
        assert value == 360
