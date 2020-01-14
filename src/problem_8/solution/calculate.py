
def get_largest_product_of_adjacent_digits(number, num_adjacent_digits):
    number_string = str(number)
    if num_adjacent_digits > len(number_string):
        raise Exception("Number of adjacent digits cannot be larger than the length of the number")

    if num_adjacent_digits < 2:
        raise Exception("Number of adjacent digits must be greater than 1")

