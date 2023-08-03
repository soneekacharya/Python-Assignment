# Define the function to convert a string to uppercase
def to_uppercase(string):
    return string.upper()

def convert_to_uppercase(strings_list):
    """
    Convert all strings in the input list to uppercase using map function.

    Args:
        strings_list (list): A list of strings.

    Returns:
        list: A new list with all strings converted to uppercase.
    """
    uppercase_list = list(map(to_uppercase, strings_list))
    return uppercase_list

input_list = ['hello', 'world']
result = convert_to_uppercase(input_list)
print(result)
