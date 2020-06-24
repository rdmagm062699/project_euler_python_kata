from .number import get_factorial, get_sum_of_digits

def get_sum_of_digits_of_a_factorial(number):
    factorial = get_factorial(number)

    return get_sum_of_digits(factorial)
