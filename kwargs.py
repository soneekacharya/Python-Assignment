def calculate_total_cost(**kwargs):
    """
    Calculate the total cost of items purchased from a store.

    Args:
        **kwargs: Arbitrary keyword arguments for items and their respective prices.

    Returns:
        float: The total cost of all items.
    """
    total_cost = sum(kwargs.values())
    return total_cost

total_cost = calculate_total_cost(laptop=150000, mouse=4000, keyboard=6000)
print(total_cost)
