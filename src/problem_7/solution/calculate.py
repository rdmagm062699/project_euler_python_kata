
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
        if _is_prime_number(next_value, primes):
            primes.append(next_value)
        if add_value > 0:
            multiplier += 1
        add_value *= -1
    
    return primes

def _is_prime_number(number, current_primes):
    is_prime = True
    for divisor in current_primes:
        if number % divisor == 0:
            is_prime = False
            break

    return is_prime