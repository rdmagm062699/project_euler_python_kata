
def get_sum_of_squares(max_number):
    squares = [number ** 2 for number in range(1, max_number + 1)]
    return sum(squares)
