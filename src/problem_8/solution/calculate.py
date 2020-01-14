
def get_largest_sum_of_adjacent_digits(number, num_adjacent_digits):
    number_string = str(number)
    if num_adjacent_digits > len(number_string):
        raise Exception("Number of adjacent digits cannot be larger than the length of the number")

    return int(max(number_string))
