
def get_largest_sum_of_adjacent_digits(number, num_adjacent_digits):
    if num_adjacent_digits > len(str(number)):
        raise Exception("Number of adjacent digits cannot be larger than the length of the number")

    return number
