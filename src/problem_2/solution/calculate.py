from .fibonacci import get_fibonacci_up_to
from .data import sum_even_numbers

def get_sum_of_even_numbers_in_fibonacci_sequence(upper_bound):
    fibonacci = get_fibonacci_up_to(upper_bound)
    return sum_even_numbers(fibonacci)
