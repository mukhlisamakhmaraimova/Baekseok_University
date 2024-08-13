# assignment_2

import os

# list all files in the current working directory
for file in os.listdir():
    if os.path.isfile(file):
        print(file)