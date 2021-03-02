import unittest

from problem_42.solution.triangle_number import is_triangle_number


class TestTriangleNumber(unittest.TestCase):

    def test_zero_is_not_a_triangle_number(self):
        self.assertEqual(is_triangle_number(0), False)
