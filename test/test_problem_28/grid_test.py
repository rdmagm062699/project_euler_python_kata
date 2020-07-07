import unittest

from problem_28.solution.grid import Grid 

class TestBuildGrid(unittest.TestCase):

    def test_spiral_in_a_3_by_3_grid(self):
        expected = [
            [7, 8, 9],
            [6, 1, 2],
            [5, 4, 3]
        ] 
        self.assertEqual(Grid().build_spiral(3), expected)


    def test_spiral_in_a_5_by_5_grid(self):
        expected = [
            [21, 22, 23, 24, 25],
            [20, 7, 8, 9, 10], 
            [19, 6, 1, 2, 11],
            [18, 5, 4, 3, 12],
            [17, 16, 15, 14, 13]
        ]

        self.assertEqual(Grid().build_spiral(5), expected)
