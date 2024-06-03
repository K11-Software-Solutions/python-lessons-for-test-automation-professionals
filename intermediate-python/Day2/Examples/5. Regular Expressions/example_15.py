import re

string = "COVID-19 lockdowns were a major influence of \
  transition to hybrid work."

# check if 'COVID-19' is at the beginning
match = re.search('\ACOVID-19', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  
