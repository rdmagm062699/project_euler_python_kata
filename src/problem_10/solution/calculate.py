
def get_sum_of_primes_less_than_n(n):
    if n <= 2:
        return 0
    
    primes = _get_primes_less_than_n(n)
    return sum([x for x in primes if x < n])


def _get_primes_less_than_n(n):
    check = [True for i in range(n+1)]
    possiblePrime = 2
    while (possiblePrime**2 <= n):
        if (check[possiblePrime] == True):
            for i in range(possiblePrime**2, n+1, possiblePrime):
                check[i] = False
        possiblePrime += 1

    return [idx for (idx,value) in enumerate(check) if idx >= 2 and value == True]
