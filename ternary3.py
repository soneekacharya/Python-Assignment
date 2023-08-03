def check_leap_year(year):
    """
    Check if the input year is a leap year using a ternary operator.

    Args:
        year (int): The year to be checked.

    Returns:
        str: "Leap Year" if the year is a leap year, "Not a Leap Year" otherwise.
    """
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return "Leap Year" if is_leap_year else "Not a Leap Year"


print(check_leap_year(2020)) 
print(check_leap_year(1700))