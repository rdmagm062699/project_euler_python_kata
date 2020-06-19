
def get_number_of_divisors(number):
    result = 0

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            result += 1

    return result
