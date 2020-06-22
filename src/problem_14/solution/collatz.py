
def get_sequence(starting_number):
    next_number = starting_number
    sequence = [next_number]
    stop = False

    while stop == False:
        next_number = _get_next_number(next_number)
        sequence.append(next_number)
        stop = True if next_number <= 1 else False

    return sequence


def _get_next_number(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1