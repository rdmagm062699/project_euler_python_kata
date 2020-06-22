import pytest

from problem_14.solution.collatz import get_sequence

class TestGetCollatzSequence:

    def test_sequence_starting_at_2(self):
        starting_number = 2
        sequence = get_sequence(starting_number)
        assert sequence == [2, 1], 'got {}'.format(sequence)
