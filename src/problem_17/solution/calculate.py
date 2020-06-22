from .numbers import get_number_name, count_letters_in_name


def get_number_of_letters_in_number_names_from_1_to_n(n):
    number_name = get_number_name(n)

    return count_letters_in_name(number_name)