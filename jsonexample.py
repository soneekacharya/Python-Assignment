""" Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data 
from the file, add the new dictionary to it, and write the updated data back to the same file. """

import json

def add_to_json(filename, new_data):
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)

        json_data.append(new_data)

        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
            
        print("Data added successfully to", filename)
    except Exception as e:
        print("Error:", e)

new_entry = {
    "name": "Shyam",
    "age": 40
}

add_to_json("sample.json", new_entry)
