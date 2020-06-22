import pytest

from problem_14.solution.calculate import get_longest_collatz_sequence

class TestGetLongestCollatzSequence:

    def test_longest_sequence_with_max_starting_number_1(self):
        value = get_longest_collatz_sequence(1)
        assert value == 1, 'got {}'.format(value)
