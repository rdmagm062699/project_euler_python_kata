import pytest

from problem_8.solution.calculate import get_largest_product_of_adjacent_digits

class TestCalculate:
    def test_number_of_adjacent_digits_must_be_less_than_length_of_number(self):
       with pytest.raises(Exception) as e:
           get_largest_sum_of_adjacent_digits(number=11, num_adjacent_digits=3)
           assert e == "Number of adjacent digits cannot be larger than the length of the number"
    
    def test_number_of_digits_must_be_greater_than_1(self):
       with pytest.raises(Exception) as e:
           get_largest_sum_of_adjacent_digits(number=11, num_adjacent_digits=1)
           assert e == "Number of adjacent digits must be greater than 1"

    def test_max_product_of_2_adjacent_digits_in_a_2_digits_number_is_expected_value(self):
        value = get_largest_product_of_adjacent_digits(44, 2)
        assert value == 16, "got {}".format(value)
