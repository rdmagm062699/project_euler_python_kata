import unittest

from problem_22.solution.calculate import score_list_of_names 

class TestScoreListOfNames(unittest.TestCase):

    def test_list_with_only_name_A(self):
        self.assertEqual(score_list_of_names(['A']), 1)
