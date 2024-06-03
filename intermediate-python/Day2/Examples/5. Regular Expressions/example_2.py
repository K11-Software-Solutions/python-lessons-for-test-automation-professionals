import re

pattern = '[abc.]'
text = 'I am a regular expression.'
print(re.findall(pattern,text))