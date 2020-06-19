from .rows import get_max_product_from_all_rows
from .colulmns import get_max_product_from_all_columns
from .diagonals import get_max_product_from_all_diagonals

def get_max_product_from_adjacent_quads(grid):
    values = [
        get_max_product_from_all_rows(grid),
        get_max_product_from_all_columns(grid),
        get_max_product_from_all_diagonals(grid)
    ]

    return max(values)
