""" Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd."""

def check_odd_even(number):
    """
    Check if the input number is odd or even using a ternary operator.

    Args:
        number (int): An integer.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    """
    return "Even" if number % 2 == 0 else "Odd"

print(check_odd_even(5)) 
print(check_odd_even(10)) 


""" Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."""

def find_bigger_number(a, b, c):
    """
    Find the larger number among the three integers using a ternary operator.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int or str: The larger number among a, b, and c, or "Equal" if they are all equal.
    """
    max_number = a if (a >= b and a >= c) else b if (b >= a and b >= c) else c
    return max_number if max_number != a or max_number != b or max_number != c else "Equal"

print(find_bigger_number(5, 10, 3))
print(find_bigger_number(8, 8, 8))


"""Create a Python function check_leap_year that takes a year as input and uses a
ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
"Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
but not divisible by 400)."""

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