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