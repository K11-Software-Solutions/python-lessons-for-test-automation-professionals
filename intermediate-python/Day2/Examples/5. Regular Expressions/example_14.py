# Program to remove all whitespaces
import re

# multiline string
phone_number = '673 9374 893'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
new_phone_number = re.sub(pattern, replace, phone_number) 
print(new_phone_number)