""" Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older."""

import csv

def filter_adults(input_file, output_file):
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.DictReader(csv_in)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if int(row['Age']) >= 18:
                writer.writerow(row)

input_file = "data.csv"
output_file = "adults.csv"
filter_adults(input_file, output_file)
print("Filtered adults saved to 'adults.csv'")
