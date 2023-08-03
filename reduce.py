from functools import reduce

def calculate_factorial(n):
    """
    Calculate the factorial of the input integer using the reduce function.

    Args:
        n (int): An integer.

    Returns:
        int: The factorial of the input number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n+1))
    
result = calculate_factorial(5)
print(result)
