from .calculate import get_pythagorean_triple_product, get_triple_where_sum_is_n

def get_product_of_triple_where_sum_is_n(n):
    triple = get_triple_where_sum_is_n(n)
    return get_pythagorean_triple_product(triple)
