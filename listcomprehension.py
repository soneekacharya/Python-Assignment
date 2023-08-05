""" Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension."""

list = ["apple", "banana", "orange", "grapefruit", "kiwi", "watermelon"]
result_list = [word for word in list if len(word) > 5]
print(result_list)


""" Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.
"""

list1 = [2, 4, 6, 8]
list2 = [3, 1, 5, 2]
product_list = [list1[i] * list2[i] for i in range(len(list1))]
print(product_list)