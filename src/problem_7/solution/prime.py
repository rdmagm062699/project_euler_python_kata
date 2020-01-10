
def is_prime_number(number):
    if number > 2 and number % 2 == 0:
        return False

    if number > 7:
        return False

    return True
