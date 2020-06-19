
def get_primes(number):
    primes = []
    next_prime = 2
    while next_prime < number:
        if number % next_prime == 0:
            primes.append(next_prime)
            number = number / next_prime
            next_prime = 2
        else:
            next_prime += 1

    primes.append(number)

    return primes
