

def get_sum_of_digits(number):
    digits = map(int, str(number))

    return sum(digits)

def get_factorial(number):
    result = 1

    for n in range(1, number + 1):
        result *= n 

    return result
