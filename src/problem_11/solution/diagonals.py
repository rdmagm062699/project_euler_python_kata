from .quads import get_max_product_of_adjacent

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
            if _is_valid_forward_diagonal(coord[X], coord[Y], len(grid), len(grid[0])):
                diagonals.append(
                    [
                        grid[coord[X]][coord[Y]],
                        grid[coord[X] + 1][coord[Y] + 1],
                        grid[coord[X] + 2][coord[Y] + 2],
                        grid[coord[X] + 3][coord[Y] + 3],
                    ]
                )

            if _is_valid_backward_diagonal(coord[X], coord[Y], len(grid)):
                diagonals.append(
                    [
                        grid[coord[X]][coord[Y]],
                        grid[coord[X] + 1][coord[Y] - 1],
                        grid[coord[X] + 2][coord[Y] - 2],
                        grid[coord[X] + 3][coord[Y] - 3],
                    ]
                )

    return diagonals

def _is_valid_forward_diagonal(x_coord, y_coord, num_rows, num_cols):
    return x_coord + 3 < num_rows and y_coord + 3 < num_cols

def _is_valid_backward_diagonal(x_coord, y_coord, num_rows):
    return x_coord + 3 < num_rows and y_coord - 3 >= 0
