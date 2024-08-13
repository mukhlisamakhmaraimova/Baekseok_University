# task_1
# first of all module of "re" is imported
import re

# define the regular expression pattern for password strength
def check_password_strength(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'

# use the re.match() function to check if the password matches the pattern
    if re.match(pattern, password):
        return "Strong password"
    else:
        return "Weak password"

# Test the password strength checker
password1 = "Password123@"
password2 = "weakpass"
password3 = "StrongPass123"

print(check_password_strength(password1))  # Output: Strong password
print(check_password_strength(password2))  # Output: Weak password
print(check_password_strength(password3))  # Output: Strong password
