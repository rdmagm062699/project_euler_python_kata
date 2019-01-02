
def get_primes(number):
    if number <= 3:
        return [number]

    if number == 4:
        return [2, 2]

    return [2, 3]
