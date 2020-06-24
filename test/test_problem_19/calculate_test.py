import unittest

from problem_19.solution.calculate import count_first_of_month_sundays_for_range_of_years

class TestFirstMonthSundaysForRange(unittest.TestCase):
    
    def test_2000_to_2001_has_3_sundays_on_the_first_of_the_month(self):
        self.assertEqual(count_first_of_month_sundays_for_range_of_years(2000, 2001), 3)
  
