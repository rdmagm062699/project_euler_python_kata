
def get_sum_of_primes_less_than_n(n):
    if n <= 2:
        return 0
    
    primes = [2,3]
    return sum([x for x in primes if x < n])