import unittest

from problem_18.solution.calculate import get_max_path_down_triangle_of_numbers

class TestMaxPathDownTriangleOfNumbers(unittest.TestCase):

    def test_single_row_with_2_is_2(self):
        triangle = [
            [2]
        ]
        self.assertEqual(get_max_path_down_triangle_of_numbers(triangle), 2);