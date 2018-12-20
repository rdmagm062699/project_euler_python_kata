import pytest

from problem_1.data import get_eligible_numbers

class TestData:

    def test_get_eligible_numbers_returns_empty_list_for_less_than_3(self):
        numbers = get_eligible_numbers(2)
        assert numbers == []

    def test_get_eligible_numbers_returns_expected_for_3(self):
        numbers = get_eligible_numbers(3)
        assert numbers == [3]
