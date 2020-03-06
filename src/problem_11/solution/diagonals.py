from src.problem_11.solution.quads import get_max_product_of_adjacent

def get_max_product_from_all_diagonals(grid):
    diagonal = [grid[x][x] for x in range(0, len(grid))]
    return get_max_product_of_adjacent(diagonal)
