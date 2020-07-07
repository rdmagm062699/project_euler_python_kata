
class Spiral:
    def __init__(self, grid_size):
        self.grid = self._build_initial_grid(grid_size)

        middle = int(len(self.grid) / 2)

        self._right_boundary = middle + 1
        self._bottom_boundary = middle + 1
        self._left_boundary = middle - 1
        self._top_boundary = middle - 1
        self._next_move = "right"
        self._move_to_pos = (middle, middle)
        self._build_spiral()

    def _build_spiral(self):
        next_number = 1

        while self._move_to_pos != (0, len(self.grid)):
            row = self._move_to_pos[0]
            col = self._move_to_pos[1]

            self.grid[row][col] = next_number

            next_number += 1

            move_direction = self._next_move
            self._calculate_next_move(move_direction, row, col)


    def _calculate_next_move(self, move_direction, row, col):
            if move_direction == "right":
                self._move_to_pos = (row, col + 1)

                if self._move_to_pos[1] == self._right_boundary:
                    self._right_boundary += 1
                    self._next_move = "down"
                else:
                    self._next_move = "right"

            elif move_direction == "down":
                self._move_to_pos = (row + 1, col)

                if self._move_to_pos[0] == self._bottom_boundary:
                    self._bottom_boundary += 1
                    self._next_move = "left"
                else:
                    self._next_move = "down"

            elif move_direction == "left":
                self._move_to_pos = (row, col - 1)

                if self._move_to_pos[1] == self._left_boundary:
                    self._left_boundary -= 1
                    self._next_move = "up"
                else:
                    self._next_move = "left"

            elif move_direction == "up":
                self._move_to_pos = (row - 1, col)

                if self._move_to_pos[0] == self._top_boundary:
                    self._top_boundary -= 1
                    self._next_move = "right"
                else:
                    self._next_move = "up"


    def _build_initial_grid(self, grid_size):
        grid = []

        for row in range(0, grid_size):
            grid.append([])
            for col in range(0, grid_size):
                grid[row].append(0)

        return grid
