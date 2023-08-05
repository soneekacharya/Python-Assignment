""" Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.
"""

def divide(num1, num2):
    """
    Perform division of two numbers.

    This function takes two integers as input (num1 and num2) and returns
    the result of the division (num1 / num2). If the second integer (num2) is
    zero, a custom error message will be displayed

    Args:
    num1(int): The first integer (divisor).
    num1(int): The second integer(dividend).

    Returns:
    float: The result of the division if num2 is not zero.

    Raises:
    ZeroDivisionError: If the second integer is zero.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print("Error: Division By Zero")
        result = None
    return result

print(divide(9, 0))
print(divide(9, 3))


"""  Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages. """

def divide_numbers():
        try:
            num1 = int(input("Enter the first integer: "))
            num2 = int(input("Enter the second integer: "))

            result = num1 / num2
            print("Result of division: ", result)

        except ValueError:
            print("Error: Please enter valid integers.")
        except ZeroDivisionError as e:
            print("Error: Division By Zero")

divide_numbers()

""" Write a Python program that takes a user input and converts it to an integer. Handle
the ValueError and display a custom error message when the input cannot be
converted to an integer."""

def convert_to_integer(user_input):
    try:
        num = int(user_input)
        print(f"Successfully converted to an integer: {num}")
    except ValueError:
        print("Error: Input cannot be converted to an integer.")

user_input = input("Enter a number: ")
convert_to_integer(user_input)
