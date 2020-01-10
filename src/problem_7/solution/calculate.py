
def get_nth_prime_number(n):
    if n <= 2:
        return n + 1

    primes = [2, 3]
    next_num = 4
    next_multplier = 1
    next_add = -1
    while len(primes) < n:
        if (6 * next_multplier) + next_add == next_num:
            primes.append(next_num)
            if next_add > ~0:
                next_multplier += 1
            next_add *= -1

        next_num += 1    

    return primes[-1]
    