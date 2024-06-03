# Braces match repeating patterns in a sequence
import re

pattern = 'a{1,3}' # At least 1 a and at most 3 a's
text = ['abion aaaaand brian','ab road aab caaat']
for t in text:
    num_matches = re.findall(pattern, t)
    print(num_matches,':',t)

print(re.findall(pattern, 'abion and brian aaat'))