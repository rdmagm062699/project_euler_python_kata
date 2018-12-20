import pytest

from problem_1.data import get_eligible_numbers

class TestData:

    def test_get_eligible_numbers_returns_empty_list_for_less_than_or_equal_to_3(self):
        numbers = get_eligible_numbers(3)
        assert numbers == []

    def test_get_eligible_numbers_returns_expected_for_4(self):
        numbers = get_eligible_numbers(4)
        print(numbers)
        assert numbers == [3]

    def test_get_eligible_numbers_returns_expected_for_6(self):
        numbers = get_eligible_numbers(6)
        assert numbers == [3, 5]

    def test_get_eligible_numbers_returns_expected_for_18(self):
        numbers = get_eligible_numbers(18)
        assert numbers == [3, 5, 6, 9, 10, 12, 15]
