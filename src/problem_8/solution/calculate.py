
def get_largest_product_of_adjacent_digits(number, num_adjacent_digits):
    digits = [int(digit) for digit in str(number)]
    _validate(digits, num_adjacent_digits)

    return digits[0] * digits[1]

    
def _validate(digits, num_adjacent_digits):
    if num_adjacent_digits > len(digits):
        raise Exception(
            "Number of adjacent digits cannot be larger than the length of the number")

    if num_adjacent_digits < 2:
        raise Exception("Number of adjacent digits must be greater than 1")

