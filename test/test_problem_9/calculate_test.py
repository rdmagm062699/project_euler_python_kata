import pytest

from problem_9.solution.calculate import get_nth_primitave_pythagorean_triple, get_pythagorean_triple_sums

class TestPrimitavePythagoreanTriples:
    def test_get_first_primitave_pythagorean_triple(self):
       value = get_nth_primitave_pythagorean_triple(1)
       assert value == (3,4,5), "got {}".format(value)

    def test_get_second_primative_pythagorean_triple(self):
       value = get_nth_primitave_pythagorean_triple(2)
       assert value == (5, 12, 13), "got {}".format(value)

    def test_get_third_primative_pythagorean_triple(self):
       value = get_nth_primitave_pythagorean_triple(3)
       assert value == (7, 24, 25), "got {}".format(value)

class TestPythagoreanTripleSums:
    def test_sum_of_pythagorean_triple_with_stop_value_13(self):
        triple = (3, 4, 5)
        value = get_pythagorean_triple_sums(triple, 13)
        assert value == (3, 4, 5), "got {}".format(value)

    def test_sum_of_pythagorean_triple_with_stop_value_36(self):
        triple = (3, 4, 5)
        value = get_pythagorean_triple_sums(triple, 36)
        assert value == (9, 12, 15), "got {}".format(value)
