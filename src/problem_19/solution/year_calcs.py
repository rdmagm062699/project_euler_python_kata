import datetime

def count_first_of_month_sundays(year):
    count = 0

    for month in range(1, 13):
        checkdate = datetime.datetime(year, month, 1)
        count += 1 if checkdate.weekday() == 6 else 0

    return count
