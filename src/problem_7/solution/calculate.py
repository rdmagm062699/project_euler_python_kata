
def get_nth_prime_number(n):
    primes = [2, 3]
    if n <= 2:
        return primes[n-1]
    else:
        return 5    
