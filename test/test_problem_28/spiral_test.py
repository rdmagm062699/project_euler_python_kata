import unittest

from problem_28.solution.spiral import Spiral 

class TestSpiral(unittest.TestCase):

    def test_spiral_in_a_3_by_3_grid(self):
        expected = [
            [7, 8, 9],
            [6, 1, 2],
            [5, 4, 3]
        ] 
        self.assertEqual(Spiral(3).grid, expected)


    def test_spiral_in_a_5_by_5_grid(self):
        expected = [
            [21, 22, 23, 24, 25],
            [20, 7, 8, 9, 10], 
            [19, 6, 1, 2, 11],
            [18, 5, 4, 3, 12],
            [17, 16, 15, 14, 13]
        ]

        self.assertEqual(Spiral(5).grid, expected)

    def test_sum_of_diagonals_in_a_3_by_3_grid_is_26(self):
        spiral = Spiral(3)

        self.assertEqual(spiral.sum_of_diagonals(), 26)
