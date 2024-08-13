# task_3

# first of all module of "re" is imported
import re

# Define the regular expression pattern for extracting URLs
def extract_urls(input_string):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+|www\.(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

# use the re.findall() function to find all matches of the pattern in the input string
    urls = re.findall(pattern, input_string)

    return urls


# Test the URL extractor
input_string = "Check out my website at https://www.example.com. You can also visit http://google.com for more information."
print(extract_urls(input_string))  # Output: ['https://www.example.com', 'http://google.com']
