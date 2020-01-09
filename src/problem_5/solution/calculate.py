from .processor import check_all_divisors

def get_smallest_number_divisible_by_range(max_divisor):
    done = False
    multiplier = 0
    while done == False:
        multiplier += 1
        dividend = max_divisor * multiplier
        if check_all_divisors(dividend, max_divisor - 1):
            done = True

    return dividend
