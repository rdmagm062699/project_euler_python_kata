import pytest

from src.problem_11.solution.rows import get_max_product_from_all_rows

class TestGetMaxProductFromAllRows:
    def test_one_row_returns_product_of_that_row(self):
        grid = [[1,2,3,4]]
        value = get_max_product_from_all_rows(grid)
        assert value == 24
