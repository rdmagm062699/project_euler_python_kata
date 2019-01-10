import pytest

from problem_4.solution.calculate import get_largest_palindrome

class TestGetLargestPalindrome:

    def test_get_largest_palindrome_for_1_digit(self):
        value = get_largest_palindrome(1)
        assert value == 9

    def test_get_largest_palindrome_for_2_digit(self):
        value = get_largest_palindrome(2)
        assert value == 9009
