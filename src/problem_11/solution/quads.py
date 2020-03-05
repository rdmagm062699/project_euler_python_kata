
def get_max_product_of_adjacent(list_of_numbers):
    max_value = 0
    start = 0
    while len(list_of_numbers[start:start+4]) == 4:
        value = _get_product(list_of_numbers[start:start+4])
        if value > max_value:
            max_value = value
        start += 1

    return max_value

def _get_product(list_of_numbers):
    value = 1
    for number in list_of_numbers:
        value = value * number
    return value
