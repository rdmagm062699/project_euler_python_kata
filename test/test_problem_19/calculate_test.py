import unittest

from problem_19.solution.year_calcs import count_first_of_month_sundays

class TestFirstMonthSundays(unittest.TestCase):
    
    def test_2000_has_3_sundays_on_the_first_of_the_month(self):
        self.assertEqual(count_first_of_month_sundays(2000), 3)

    def test_2001_has_2_sundays_on_the_first_of_the_month(self):
        self.assertEqual(count_first_of_month_sundays(2001), 2)
