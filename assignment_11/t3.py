#task3

# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If the year is divisible by 4 and not by 100, or if it is divisible by 400, it is a leap year
    print(year, "is a leap year")
else:
    # Otherwise, it is not a leap year
    print(year, "is not a leap year")