
class NumberTriangle:
    def __init__(self, rows):
        self.rows = rows

    def get_max_path_down(self):
        max_pos_tracker = [[0]]

        for row_num in range(1, len(self.rows)):
            prev_positions = max_pos_tracker[row_num - 1]
            current_row = self.rows[row_num]

            positions_to_check = set()
            for pos in prev_positions:
                positions_to_check.add(pos)
                positions_to_check.add(pos + 1)

            values_to_check = [value for (idx, value) in enumerate(current_row) if idx in positions_to_check]
            max_value = max(values_to_check)
            max_positions = [pos for pos in positions_to_check if current_row[pos] == max_value]
            max_pos_tracker.append(max_positions)

        max_values = [self.rows[idx][pos[0]] for (idx,pos) in enumerate(max_pos_tracker)]
        return sum(max_values)
