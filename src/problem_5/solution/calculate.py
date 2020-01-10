from .processor import check_all_divisors, get_divisors_to_check

def get_smallest_number_divisible_by_range(max_divisor):
    done = False
    multiplier = 0
    dividend_increase_by = max_divisor
    divisors = get_divisors_to_check(max_divisor)

    while done == False:
        multiplier += 1
        dividend = dividend_increase_by * multiplier
        if check_all_divisors(dividend, divisors):
            done = True

    return dividend
