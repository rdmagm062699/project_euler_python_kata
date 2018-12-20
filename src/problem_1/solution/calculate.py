from .data import get_eligible_numbers

def get_sum_of_numbers_divisible_by_three_and_five(max_number):
    numbers = get_eligible_numbers(max_number)
    return sum(numbers)
