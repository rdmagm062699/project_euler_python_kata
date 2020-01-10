import pytest

from problem_6.solution.problem import solve_difference_square_of_sum_and_sum_of_square

class TestProblem:
    def test_problem_solve_for_10(self):
        value = solve_difference_square_of_sum_and_sum_of_square(max_number=10)
        assert value == 2640 
