""" Create a function search_log that takes a log file and a search keyword as input.
The function should find and display all lines containing the search keyword.
"""

def search_log(log_file, search_keyword):
    with open(log_file, 'r') as file:
        for line in file:
            if search_keyword in line:
                print(line.strip())

log_file = "example.log"
search_keyword = "ERROR"
search_log(log_file, search_keyword)


""" Using generator"""

def search_log(log_file, search_keyword):
    with open(log_file, 'r') as file:
        for line in file:
            if search_keyword in line:
                yield line.strip()

log_file = "example.log"
search_keyword = "ERROR"

for line in search_log(log_file, search_keyword):
    print(line)