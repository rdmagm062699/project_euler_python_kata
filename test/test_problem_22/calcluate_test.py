import unittest

from problem_22.solution.calculate import score_list_of_names 

class TestScoreListOfNames(unittest.TestCase):

    def test_list_with_only_name_A(self):
        self.assertEqual(score_list_of_names(['A']), 1)

    def test_list_with_names_A_B(self):
        self.assertEqual(score_list_of_names(['A', 'B']), 5)

    def test_list_with_names_A_B_C(self):
        self.assertEqual(score_list_of_names(['A', 'B', 'C']), 14)

    def test_list_is_sorted_before_scoring(self):
        self.assertEqual(score_list_of_names(['C', 'A', 'B']), 14)