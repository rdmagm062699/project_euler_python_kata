
def get_max_product_of_adjacent(list_of_numbers):
    value = 1
    for number in list_of_numbers:
        value = value * number
    return value
