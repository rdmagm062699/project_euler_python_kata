
def get_triple_where_sum_is_n(n):
    result = None

    a = 1
    while not result and a < n:
        b = a
        while b < n - a:
            c = n - a - b

            if _is_pythagorean_triple(a, b, c):
                result = (a, b, c)
                break

            b += 1

        if result:
            break

        a += 1
    
    return result

def _is_pythagorean_triple(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)

def get_pythagorean_triple_product(triple):
    pass
