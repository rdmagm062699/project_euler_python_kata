import pytest

from problem_8.solution.calculate import get_largest_sum_of_adjacent_digits

class TestCalculate:
    def test_number_of_adjacent_digits_must_be_less_than_length_of_number(self):
       with pytest.raises(Exception):
           get_largest_sum_of_adjacent_digits(number=1, num_adjacent_digits=2)
    
    def test_get_largest_sum_of_1_adjacent_digit_within_a_single_digit_number_is_that_number(self):
        number = 5
        assert get_largest_sum_of_adjacent_digits(number, num_adjacent_digits=1) == number
