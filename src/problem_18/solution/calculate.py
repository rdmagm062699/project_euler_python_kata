
class NumberTriangle:
    def __init__(self, rows):
        self.rows = rows

    def get_max_path_down(self):
        triangle = self.rows

        for row in reversed(range(0, len(triangle) - 1)):
            for col in range(0, len(triangle[row])):
                values = [triangle[row + 1][col], triangle[row + 1][col + 1]]
                triangle[row][col] += max(values)

        return triangle[0][0]
