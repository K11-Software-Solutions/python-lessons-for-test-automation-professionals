import re

pattern = '^a.....d$'
test_string = 'android'
result = re.match(pattern, test_string)

if result:
  print("Pattern matched.")
else:
  print("No match found.")	
