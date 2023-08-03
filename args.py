def sum_numbers(*args):
    """
    Calculate the sum of an arbitrary number of numbers.

    Args:
        *args: An arbitrary number of positional arguments (numbers).

    Returns:
        int: The sum of all the numbers.
    """
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))  
print(sum_numbers(10, 20, 30))