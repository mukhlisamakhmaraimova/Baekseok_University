# Assignment 1 Create the four basic arithmetic operations: addition, subtraction, multiplication, and division as a function and
# then you can import the four basic arithmetic functions.

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Cannot divide by zero!"
    return a/b