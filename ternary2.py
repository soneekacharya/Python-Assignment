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
