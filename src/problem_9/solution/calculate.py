
def get_nth_primitave_pythagorean_triple(n):
    m = 2 + (n - 1)
    n = 1 + (n - 1)

    a = (m ** 2) - (n ** 2)
    b = 2 * (m * n)
    c = (m ** 2) + (n ** 2)

    return (a, b, c)

def get_pythagorean_triple_sums(initial_triple, stop_value):
    i = 1
    next_triple = (initial_triple[0] * i, initial_triple[1] * i, initial_triple[2] * i)
    while sum(next_triple) < stop_value:
        i += 1
        next_triple = (initial_triple[0] * i, initial_triple[1] * i, initial_triple[2] * i)

    return next_triple
