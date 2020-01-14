import pytest

from problem_9.solution.calculate import get_nth_primitave_pythagorean_triple

class TestPrimitavePythagoreanTriples:
    def test_get_first_primitave_pythagorean_triple(self):
       value = get_nth_primitave_pythagorean_triple(1)
       assert value == (3,4,5), "got {}".format(value)
