from .numbers import get_number_name, count_letters_in_name


def get_number_of_letters_in_number_names_from_1_to_n(n):
    counts = []

    for number in range(1, n + 1):
        number_name = get_number_name(number)
        counts.append(count_letters_in_name(number_name))

    return sum(counts)
