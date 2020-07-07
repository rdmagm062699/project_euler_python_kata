
class Spiral:
    def __init__(self, grid_size):
        self.grid = self._build_initial_grid(grid_size)
        self._build_spiral()

    def _build_spiral(self):
        middle = int(len(self.grid) / 2)

        right_boundary = middle + 1
        bottom_boundary = middle + 1
        left_boundary = middle - 1
        top_boundary = middle - 1
        next_move = "right"
        next_number = 1
        current_pos = (middle, middle)

        while current_pos != (0, len(self.grid)):
            row = current_pos[0]
            col = current_pos[1]

            self.grid[row][col] = next_number

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


    def _build_initial_grid(self, grid_size):
        grid = []

        for row in range(0, grid_size):
            grid.append([])
            for col in range(0, grid_size):
                grid[row].append(0)

        return grid
