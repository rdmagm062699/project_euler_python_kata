from src.problem_11.solution.quads import get_max_product_of_adjacent

def get_max_product_from_all_rows(grid):
    max_value = 0
    for row in grid:
        value = get_max_product_of_adjacent(row)
        if value > max_value:
            max_value = value

    return max_value
