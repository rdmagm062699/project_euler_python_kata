
def get_nth_prime_number(n):
    if n <= 2:
        return n + 1
    else:
        return _get_n_primes(n)[-1] 

def _get_n_primes(n):
    primes = [2, 3]

    multiplier = 1
    add_value = -1
    while len(primes) < n:
        next_value = (6 * multiplier) + add_value
        primes.append(next_value)
        if add_value > 0:
            multiplier += 1
        add_value *= -1
    
    return primes