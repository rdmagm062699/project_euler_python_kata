import unittest

from problem_42.solution.word import get_word_value


class TestWordValue(unittest.TestCase):

    def test_value_of_word_A(self):
        self.assertEqual(get_word_value('A'), 1)
