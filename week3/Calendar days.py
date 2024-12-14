import calendar
from datetime import datetime


def number_of_days(year, month):
    """
    A function that returns the number of calendar days in a given year and month

    Args:
        year (int): The given year
        month (int): The given month
    """
    assert isinstance(year, int) and isinstance(month, int) and year > 0 and month > 0
    _, num_days = calendar.monthrange(year, month)
    return num_days


def number_of_leap_years(year1, year2):
    """
    A function to find the number of leap-years between (including both endpoints) two given years

    Args:
        year1 (int): start year
        year2 (int): end year
    """
    assert isinstance(year1, int) and isinstance(year2, int) and year1 > 0 and year2 > 0
    ans = 0
    for i in range(min(year1, year2), max(year1, year2) + 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            ans += 1
    return ans


def get_day_of_week(year, month, day):
    """
    A function to find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year

    Args:
        year (int): Year
        month (int): Month
        day (int): Day
    """
    assert (
        isinstance(year, int)
        and isinstance(month, int)
        and isinstance(day, int)
        and year > 0
        and month > 0
        and day > 0
    )
    date = datetime(year, month, day)
    return calendar.day_name[date.weekday()]
