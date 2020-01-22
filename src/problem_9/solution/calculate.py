
def get_triple_where_sum_is_n(n):
    result = None

    a = 1
    while not result and a < n:
        b = a
        while b < n - a:
            c = n - a - b

            if (a ** 2) + (b ** 2) == (c ** 2):
                result = (a, b, c)
                break

            b += 1

        if result:
            break

        a += 1
    
    return result
