from src.problem_11.solution.quads import get_max_product_of_adjacent

def get_max_product_from_all_diagonals(grid):
    max_value = 0
    for diagonal in _get_all_diagonals(grid):
        value = get_max_product_of_adjacent(diagonal)
        if value > max_value:
            max_value = value

    return max_value

def _get_all_diagonals(grid):
    diagonal = []
    opposite = []
    for coord in [(i,i) for i in range(0, len(grid))]:
        x = coord[0]
        oppo_x = abs(len(grid) - 1 - x)
        y = coord[1]
        diagonal.append(grid[x][y])
        opposite.append(grid[oppo_x][y])

    return [diagonal, opposite]
