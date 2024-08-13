# task_1

# first of all module of "re" is imported
import re

# define the regular expression pattern for email validation
def validation_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0]+\.[a-zA-Z]{2,}$'
# use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# test the email validation function
email1 = "example@email.com"
email2 = "invalid_email@.com"
email3 = "123example@domain.org"

print(validation_email(email1))  # Output: True
print(validation_email(email2))  # Output: False
print(validation_email(email3))  # Output: True