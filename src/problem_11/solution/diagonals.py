from src.problem_11.solution.quads import get_max_product_of_adjacent

X = 0
Y = 1

def get_max_product_from_all_diagonals(grid):
    max_value = 0
    for diagonal in _get_all_diagonals(grid):
        value = get_max_product_of_adjacent(diagonal)
        if value > max_value:
            max_value = value

    return max_value

def _get_all_diagonals(grid):
    diagonals = []
    for row in range(0, len(grid)):
        for coord in [(row,col) for col in range(0, len(grid))]:
            if coord[X] + 3 < len(grid) and coord[Y] + 3 < len(grid[0]):
                diagonals.append(
                    [
                        grid[coord[X]][coord[Y]],
                        grid[coord[X] + 1][coord[Y] + 1],
                        grid[coord[X] + 2][coord[Y] + 2],
                        grid[coord[X] + 3][coord[Y] + 3],
                    ]
                )

            if coord[X] + 3 < len(grid) and coord[Y] - 3 >= 0:
                diagonals.append(
                    [
                        grid[coord[X]][coord[Y]],
                        grid[coord[X] + 1][coord[Y] - 1],
                        grid[coord[X] + 2][coord[Y] - 2],
                        grid[coord[X] + 3][coord[Y] - 3],
                    ]
                )

    return diagonals
