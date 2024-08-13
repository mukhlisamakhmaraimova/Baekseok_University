# assignmnet_3

import csv
import os

file_path = 'example.txt'

if os.path.exists(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

else:
    print(f"The file {file_path} does not exist in the current directory")


