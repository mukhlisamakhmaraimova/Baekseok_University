#task4

import calendar

# Get input from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Get day of the week
day_of_week = calendar.weekday(year, month, day)

# Map day of the week to corresponding string
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_string = days[day_of_week]

# Print result
print("The day of the week for {}/{}/{} is {}".format(month, day, year, day_string))