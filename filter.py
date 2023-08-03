def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime_numbers(numbers_list):
    """
    Filter prime numbers from the input list of integers using the filter function.

    Args:
        numbers_list (list): A list of integers.

    Returns:
        list: A new list containing only the prime numbers.

    """
    prime_numbers_iterator = filter(is_prime, numbers_list)
    prime_numbers_list = list(prime_numbers_iterator)
    return prime_numbers_list

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime_numbers(input_list)
print(result)
