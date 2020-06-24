import unittest

from problem_18.solution.calculate import NumberTriangle

class TestMaxPathDownTriangleOfNumbers(unittest.TestCase):

    def test_single_row_triangle(self):
        triangle = [
            [2]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 2)
    
    def test_simple_two_row_triangle(self):
        triangle = [
             [1],
            [2, 3]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 4)

    def test_simple_three_row_triangle(self):
        triangle = [
              [1],
             [0, 3],
            [3, 0, 1]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 5)

    def test_three_row_triangle_with_duplicate_values_on_second_row(self):
        triangle = [
              [1],
             [2, 2],
            [1, 0, 3]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 6)

    def test_three_row_triangle_with_duplicate_values_on_second_and_last_rows(self):
        triangle = [
              [1],
             [2, 2],
            [1, 3, 3]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 6)

    def test_four_row_triangle_with_duplicate_values_on_second_and_third_rows(self):
        triangle = [
               [1],
              [2, 2],
             [3, 0, 3],
            [1, 1, 1, 4]
        ]
        number_triangle = NumberTriangle(triangle)
        self.assertEqual(number_triangle.get_max_path_down(), 10)
