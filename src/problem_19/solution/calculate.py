from .year_calcs import count_first_of_month_sundays

def count_first_of_month_sundays_for_range_of_years(first_year, last_year):
    count = 0

    for year in range(first_year, last_year + 1):
        count += count_first_of_month_sundays(year)

    return count
