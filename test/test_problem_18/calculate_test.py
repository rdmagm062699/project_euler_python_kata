import unittest

from problem_18.solution.calculate import get_max_path_down_triangle_of_numbers

class TestMaxPathDownTriangleOfNumbers(unittest.TestCase):

    def test_single_row_triangle(self):
        triangle = [
            [2]
        ]
        self.assertEqual(get_max_path_down_triangle_of_numbers(triangle), 2);
    
    def test_simple_two_row_triangle(self):
        triangle = [
            [1],
            [2, 3]
        ]

    def test_simple_three_row_triangle(self):
        triangle = [
              [1],
             [0, 3],
            [3, 0, 1]
        ]
        self.assertEqual(get_max_path_down_triangle_of_numbers(triangle), 5)
