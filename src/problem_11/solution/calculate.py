from src.problem_11.solution.rows import get_max_product_from_all_rows
from src.problem_11.solution.colulmns import get_max_product_from_all_columns

def get_max_product_from_adjacent_quads(grid):
    values = [
        get_max_product_from_all_rows(grid),
        get_max_product_from_all_columns(grid)
    ]

    return max(values)
