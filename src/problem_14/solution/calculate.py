from .collatz import Collatz

def get_longest_collatz_sequence(max_starting_number):
    longest = (0, 0)

    for n in range(1, max_starting_number + 1):
        sequence = Collatz().get_sequence(n)
        if len(sequence) > longest[0]:
            longest = (len(sequence), n)
    
    return longest[1]