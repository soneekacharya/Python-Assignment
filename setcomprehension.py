""" Given a list of numbers, create a set using set
comprehension that contains only unique even numbers."""

numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]
unique_even_numbers = {num for num in numbers if num % 2 == 0}

print(unique_even_numbers)

""" Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings."""

string1 = "hello"
string2 = "world"

common_characters = {char for char in string1 if char in string2}

print(common_characters)