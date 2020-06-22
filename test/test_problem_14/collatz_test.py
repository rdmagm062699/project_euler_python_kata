import pytest

from problem_14.solution.collatz import get_sequence

class TestGetCollatzSequence:

    def test_sequence_starting_at_2(self):
        starting_number = 2
        sequence = get_sequence(starting_number)
        assert sequence == [2, 1], 'got {}'.format(sequence)

    def test_sequence_starting_at_4(self):
        starting_number = 4
        sequence = get_sequence(starting_number)
        assert sequence == [4, 2, 1], 'got {}'.format(sequence)

    def test_sequence_starting_at_3(self):
        starting_number = 3
        sequence = get_sequence(starting_number)
        assert sequence == [3, 10, 5, 16, 8, 4, 2, 1], 'got {}'.format(sequence)
