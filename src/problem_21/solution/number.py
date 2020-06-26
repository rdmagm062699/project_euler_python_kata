
def get_proper_divisors(number):
    result = []

    if number > 1:
        result.append(1)
        for div in range(2, number):
            if number % div == 0:
                result.append(div)

    return result
