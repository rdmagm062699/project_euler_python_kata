import pytest

from problem_8.solution.calculate import get_largest_product_of_adjacent_digits

class TestCalculate:
    def test_number_of_adjacent_digits_must_be_less_than_length_of_number(self):
       with pytest.raises(Exception) as e:
           get_largest_sum_of_adjacent_digits(number=1, num_adjacent_digits=2)
           assert e == "Number of adjacent digits cannot be larger than the length of the number"
