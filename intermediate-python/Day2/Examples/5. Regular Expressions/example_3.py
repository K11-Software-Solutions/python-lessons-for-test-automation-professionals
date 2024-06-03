import re

# Period
pattern = '..'
text = 'I am a regular expression.'
num_matches = len(re.findall(pattern,text))
print('Matches:',num_matches)