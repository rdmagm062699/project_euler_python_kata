import pytest

from problem_4.solution.palindrome import is_palindrome

class TestIsPalindrome: 

    def test_is_palindrome_10(self):
        test = is_palindrome(10)
        assert test == False, 'got {}'.format(test)
