# assignment_1
import csv

# create a CSV file with two columns
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])
    writer.writerow(['Bob', 30])

# read the CSV file and print its contents
with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)