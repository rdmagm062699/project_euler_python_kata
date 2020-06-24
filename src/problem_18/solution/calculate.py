
def get_max_path_down_triangle_of_numbers(triangle):
    max_sum = triangle[0][0]
    last_max_pos = 0

    for row_num in range(1, len(triangle)):
        row = triangle[row_num]
        first_possible = row[last_max_pos]
        second_possible = row[last_max_pos + 1]

        if first_possible == second_possible:
            dupe_max_pos = _handle_dupes(triangle, row_num, last_max_pos, last_max_pos + 1)
            max_sum += row[dupe_max_pos]
            last_max_pos = dupe_max_pos
        else:
            max_value = max([first_possible, second_possible])
            last_max_pos = row.index(max_value)
            max_sum += max_value

    return max_sum

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
    