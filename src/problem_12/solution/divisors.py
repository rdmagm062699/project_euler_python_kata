from .primes import get_primes

def get_number_of_divisors(number):
    result = 1

    if number > 1:
        primes = get_primes(number)
        for x in set(primes):
            result = result * (primes.count(x) + 1)

    return result
