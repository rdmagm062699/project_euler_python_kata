
def build_spiral(grid_size):
    grid = _build_grid(grid_size)
    middle = int(grid_size / 2)

    right_boundary = middle + 1
    bottom_boundary = middle + 1
    left_boundary = middle - 1
    top_boundary = middle - 1
    next_move = "right"
    next_number = 1
    current_pos = (middle, middle)

    while current_pos != (0, len(grid)):
        row = current_pos[0]
        col = current_pos[1]

        grid[row][col] = next_number

        next_number += 1

        if next_move == "right":
            current_pos = (row, col + 1)

            if current_pos[1] == right_boundary:
                right_boundary += 1
                next_move = "down"
            else:
                next_move = "right"

        elif next_move == "down":
            current_pos = (row + 1, col)

            if current_pos[0] == bottom_boundary:
                bottom_boundary += 1
                next_move = "left"
            else:
                next_move = "down"

        elif next_move == "left":
            current_pos = (row, col - 1)

            if current_pos[1] == left_boundary:
                left_boundary -= 1
                next_move = "up"
            else:
                next_move = "left"

        elif next_move == "up":
            current_pos = (row - 1, col)

            if current_pos[0] == top_boundary:
                top_boundary -= 1
                next_move = "right"
            else:
                next_move = "up"

    return grid


def _build_grid(grid_size):
    grid = []

    for row in range(0, grid_size):
        grid.append([])
        for col in range(0, grid_size):
            grid[row].append(0)

    return grid
