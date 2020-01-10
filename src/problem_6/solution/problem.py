from .calculate import get_square_of_sum, get_sum_of_squares

def solve_difference_square_of_sum_and_sum_of_square(max_number):
    return get_square_of_sum(max_number) - get_sum_of_squares(max_number)
