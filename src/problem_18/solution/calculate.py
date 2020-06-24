
def get_max_path_down_triangle_of_numbers(triangle):
    max_sum = triangle[0][0]
    last_max_pos = 0

    for row_num in range(1, len(triangle)):
        row = triangle[row_num]

        pos1 = last_max_pos
        pos2 = last_max_pos + 1

        first_possible = row[pos1]
        second_possible = row[pos2]

        if first_possible == second_possible:
            max_sum += first_possible
            if _not_last_row(row_num, triangle):
                last_max_pos = _handle_dupes(triangle, row_num, pos1, pos2)
        else:
            max_value = max([first_possible, second_possible])
            last_max_pos = row.index(max_value)
            max_sum += max_value

    return max_sum

def _not_last_row(row_num, triangle):
    return row_num < len(triangle) - 1

def _handle_dupes(triangle, row_num, pos1, pos2):
    next_row = triangle[row_num + 1]

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
    