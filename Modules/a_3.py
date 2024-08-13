# task-3

def perform_arithmetic_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = num1 / num2
    return result

num1 = 3
num2 = 4
operation = '+'
result = perform_arithmetic_operation(num1, operation, num2)
print("Result:", result)  # Output: Result: 7