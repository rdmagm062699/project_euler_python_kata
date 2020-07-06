import unittest

from problem_28.solution.spiral import build_spiral 

class TestBuildSpiral(unittest.TestCase):

    def test_spiral_in_a_3_by_3_grid(self):
        expected = [
            [7, 8, 9],
            [6, 1, 2],
            [5, 4, 3]
        ] 
        self.assertEqual(build_spiral(3), expected)

