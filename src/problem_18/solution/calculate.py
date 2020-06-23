
def get_max_path_down_triangle_of_numbers(triangle):
    max_sum = triangle[0][0]
    last_max_pos = 0

    for row_num in range(1, len(triangle)):
        row = triangle[row_num]
        max_value = max([row[last_max_pos], row[last_max_pos + 1]])
        last_max_pos = row.index(max_value)
        max_sum += max_value

    return max_sum
