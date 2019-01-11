from .data import get_possible_factors
from .palindrome import is_palindrome

def get_largest_palindrome(num_of_digits):
    left_factors = get_possible_factors(num_of_digits)
    right_factors = left_factors.copy()
    max = 0

    for factor_one in left_factors:
        for factor_two in right_factors:
            value = factor_one * factor_two
            if is_palindrome(value) and value > max:
                max = value

        right_factors.pop(0)

    return max
