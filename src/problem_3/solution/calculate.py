from .primes import get_primes

def get_highest_prime(number):
    primes = get_primes(number)
    return sorted(primes, reverse=True)[0]
