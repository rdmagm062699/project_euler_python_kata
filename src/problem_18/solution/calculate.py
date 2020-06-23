
def get_max_path_down_triangle_of_numbers(triangle):
    max_sum = triangle[0][0]

    for row_num in range(1, len(triangle)):
        row = triangle[row_num]
        max_sum += max(row)

    return max_sum
