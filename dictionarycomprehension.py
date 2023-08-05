""" Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension.
"""

keys = ["movie_name","actor","director","released_year"]
values = ["Oppenheimer","Cilian Murphy","Christopher Nolan","2023"]

result = {keys[i]:values[i] for i in range(1,len(keys))}
print(result)


"""  Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension."""

student_dict = {"John": 89, "Will": 90, "Sarah":95, "Gian":60, "Suniyo":70}

high_scores = {name:score for name,score in student_dict.items() if score>80}

print(high_scores)