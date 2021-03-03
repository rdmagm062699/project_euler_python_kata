import math

def is_triangle_number(number):
    if number <= 0:
        return False

    check_val = (number * 8) + 1
    return math.sqrt(check_val).is_integer()
