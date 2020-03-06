from src.problem_11.solution.quads import get_max_product_of_adjacent

def get_max_product_from_all_columns(grid):
    column = [row[0] for row in grid]
    return get_max_product_of_adjacent(column)
