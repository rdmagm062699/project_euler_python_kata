import unittest

from problem_17.solution.calculate import get_number_of_letters_in_number_names_from_1_to_n

class TestNumberOfLettersInNumberNames(unittest.TestCase):

    def test_max_of_1_has_3_letters(self):
        self.assertEqual(get_number_of_letters_in_number_names_from_1_to_n(1), 3)
