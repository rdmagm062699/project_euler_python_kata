from math import sqrt

def get_proper_divisors(number):
    result = []

    if number > 1:
        result.append(1)
        for div in range(2, int(sqrt(number) + 1)):
            if number % div == 0:
                result.extend([div, int(number / div)])

    return list(set(result))
