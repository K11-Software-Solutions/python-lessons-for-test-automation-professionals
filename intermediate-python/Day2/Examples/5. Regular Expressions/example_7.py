import re
# + matches zero or one occurences of a pattern
pattern = 'd?ing'
texts = ['Mixing chemicals can be dangerous.','The rate of flow gradually changed.',\
    'Paddington changed his name to Ted.',\
        'The shading of the text is different.']
for text in texts:
    num_matches = len(re.findall(pattern, text))
    print(num_matches,':',text)
