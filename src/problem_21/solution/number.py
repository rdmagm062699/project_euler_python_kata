from math import sqrt

def get_proper_divisors(number):
    result = []

    if number > 1:
        result.append(1)
        for div in range(2, int(sqrt(number) + 1)):
            if number % div == 0:
                result.extend([div, int(number / div)])

    return list(set(result))

def get_sum_of_amicable_numbers_less_than_n(n):
    value = 0

    for num in range(2, n):
        check_amicable = sum(get_proper_divisors(num))
        if num != check_amicable and num == sum(get_proper_divisors(check_amicable)):
            print("num={}, check_amicable={}".format(num, check_amicable))
            value += num

    return value
