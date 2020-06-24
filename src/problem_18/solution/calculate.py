
class NumberTriangle:
    def __init__(self, rows):
        self.rows = rows

    def get_max_path_down(self):
        max_sum = self.rows[0][0]
        last_max_pos = 0

        for row_num in range(1, len(self.rows)):
            row = self.rows[row_num]

            pos1 = last_max_pos
            pos2 = last_max_pos + 1

            first_possible = row[pos1]
            second_possible = row[pos2]

            if first_possible == second_possible:
                max_sum += first_possible
                if self._not_last_row(row_num):
                    last_max_pos = self._handle_dupes(row_num, pos1, pos2)
            else:
                max_value = max([first_possible, second_possible])
                last_max_pos = row.index(max_value)
                max_sum += max_value

        return max_sum

    def _not_last_row(self, row_num):
        return row_num < len(self.rows) - 1

    def _handle_dupes(self, row_num, pos1, pos2):
        next_row = self.rows[row_num + 1]

        first_possible = next_row[pos1]
        second_possible = next_row[pos1 + 1]
        max_value_1 = max([first_possible, second_possible])

        first_possible = next_row[pos2]
        second_possible = next_row[pos2 + 1]
        max_value_2 = max([first_possible, second_possible])

        if max_value_1 > max_value_2:
            return pos1
        else:
            return pos2
    