import unittest

from problem_42.solution.word import get_word_value, is_triangle_word


class TestWordValue(unittest.TestCase):

    def test_value_of_word_A(self):
        self.assertEqual(get_word_value('A'), 1)

    def test_value_of_word_AA(self):
        self.assertEqual(get_word_value('AA'), 2)
    
    def test_value_of_word_AAZ(self):
        self.assertEqual(get_word_value('AAZ'), 28)


class TestTriangleWord(unittest.TestCase):

    def test_A_is_triangle_word(self):
        self.assertEqual(is_triangle_word('A'), True)

    def test_AS_is_not_triangle_word(self):
        self.assertEqual(is_triangle_word('AS'), False)

    def test_SKY_is_triangle_word(self):
        self.assertEqual(is_triangle_word('SKY'), True)
