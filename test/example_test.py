import pytest

from example import example_method

class TestExample:

    def test_example(self):
        x = example_method()
        assert x == 1
