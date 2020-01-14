
def get_nth_primitave_pythagorean_triple(n):
    m = 2 + (n - 1)
    n = 1 + (n - 1)

    a = (m ** 2) - (n ** 2)
    b = 2 * (m * n)
    c = (m ** 2) + (n ** 2)

    return (a, b, c)

def get_pythagorean_triple_sums(initial_triple, stop_value):
    pass
