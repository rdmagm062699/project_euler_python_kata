from .data import get_possible_factors
from .palindrome import is_palindrome

def get_largest_palindrome(num_of_digits):
    factors = get_possible_factors(num_of_digits)
    max = 0

    for factor_one in sorted(factors, reverse=True):
        for factor_two in sorted(factors, reverse=True):
            value = factor_one * factor_two
            if is_palindrome(value) and value > max:
                max = value
                
    return max
