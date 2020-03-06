from src.problem_11.solution.quads import get_max_product_of_adjacent

def get_max_product_from_all_columns(grid):
    max_value = 0
    for column_number in range(0, len(grid[0])):
        value = get_max_product_of_adjacent(_get_column(column_number, grid))
        if value > max_value:
            max_value = value

    return max_value

def _get_column(column_number, grid):
    return [row[column_number] for row in grid]
