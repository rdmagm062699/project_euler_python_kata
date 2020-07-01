import unittest

from problem_22.solution.name import score_name 

class TestScoreName(unittest.TestCase):

    def test_name_A_with_position_1_scores_1(self):
        self.assertEqual(score_name('A', 1), 1)

    def test_name_AB_with_position_1_scores_3(self):
        self.assertEqual(score_name('AB', 1), 3)
