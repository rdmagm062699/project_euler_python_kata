
def sum_even_numbers(list_of_numbers):
    evens = [number for number in list_of_numbers if number % 2 == 0]
    return sum(evens)
