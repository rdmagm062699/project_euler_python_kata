import unittest

from problem_22.solution.name import score_name 

class TestScoreName(unittest.TestCase):

    def test_name_A_with_multiplier_1_scores_1(self):
        self.assertEqual(score_name('A', 1), 1)

    def test_name_AB_with_multiplier_1_scores_3(self):
        self.assertEqual(score_name('AB', 1), 3)

    def test_name_ABC_with_multiplier_1_scores_6(self):
        self.assertEqual(score_name('ABC', 1), 6)
