
def get_possible_factors(num_of_digits):
    lower = 10**(num_of_digits-1)
    upper = 10**(num_of_digits)
    return list(range(lower,upper))
