from .divisors import get_number_of_divisors

def find_triangular_number_divisible_by_more_than_n_numbers(n):
    count = 1
    triangular = 0
    divisors = 0

    while divisors <= n:
        triangular = triangular + count
        divisors = get_number_of_divisors(triangular)
        count += 1

    return triangular
