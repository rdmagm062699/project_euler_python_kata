
def get_largest_sum_of_adjacent_digits(number, num_adjacent_digits):
    number_string = str(number)
    if num_adjacent_digits > len(number_string):
        raise Exception("Number of adjacent digits cannot be larger than the length of the number")
    
    start = 0
    max_sum = 0
    while start + num_adjacent_digits <= len(number_string):
        numbers = [int(number) for number in number_string[start:start+num_adjacent_digits]]
        value = sum(numbers)
        if value > max_sum:
            max_sum = value
        start += 1

    return max_sum
