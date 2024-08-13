# task-4

## Expalanation: In this example, task2() will only start after task1() has completely finished its execution -> for 1st code
# In this asynchronous example, task1() and task2() are started almost simultaneously. task1() and task2() do not block the execution while
# they are in the sleeping state, allowing them to run concurrently. -> 2nd code

## Asynchronous Execution:
# Asynchronous execution, on the other hand, allows a program to handle multiple tasks seemingly at the same time. This is done by executing
# other tasks during waiting periods, such as IO operations. Python's asyncio library provides the framework for writing asynchronous code.