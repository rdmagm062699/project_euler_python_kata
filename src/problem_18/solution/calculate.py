
class NumberTriangle:
    def __init__(self, rows):
        self.rows = rows

    def get_max_path_down(self):
        max_pos_tracker = [[0]]

        for row_num in range(1, len(self.rows)):
            prev_positions = max_pos_tracker[row_num - 1]
            current_row = self.rows[row_num]

            positions_to_check = self._get_app_positions_to_check_in_current_row(prev_positions)
            max_positions = self._get_positions_of_max_values_in_current_row(current_row, positions_to_check)
            max_pos_tracker.append(max_positions)

        max_values = [self.rows[idx][pos[0]] for (idx,pos) in enumerate(max_pos_tracker)]
        return sum(max_values)

    def _get_app_positions_to_check_in_current_row(self, prev_positions):
        positions = set()
        for pos in prev_positions:
            positions.add(pos)
            positions.add(pos + 1)

        return positions

    def _get_positions_of_max_values_in_current_row(self, row, positions_to_check):
        values_to_check = [value for (idx, value) in enumerate(row) if idx in positions_to_check]
        max_value = max(values_to_check)

        return [pos for pos in positions_to_check if row[pos] == max_value]
