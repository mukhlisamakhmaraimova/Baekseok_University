#Assignmnet-2
#task1
# n = int(input("Enter: "))
# count = 0
# num = 2
# while count < n:
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             break
#     else:
#         print(num)
#         count+=1
#     num+=1

#task2
# n = int(input("Enter the number: "))
# fibonacci_sequence = [0,1]
# for i in range(2, n):
#     next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
#     fibonacci_sequence.append(next_number)
#
# print(f"The first {n} numbers in the Fibonacci sequence are: ")
# for number in fibonacci_sequence:
#     print(number, end='')


#task3
# import random
# number = random.randint(1,100)
# guess = None
# guesses_taken = 0
# while guess != number:
#     guess = int(input("Guess a number between 1 and 100: "))
#     guesses_taken += 1
#
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print(f"Congratulations! You guessed the number {number} correctly in {guesses_taken} attempts" )

#task4
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [num**2 for num in original_list if num % 2 == 0]
# print(new_list)


#task5
n = int(input("Enter a number: "))
while n != 1:
    if n % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")







