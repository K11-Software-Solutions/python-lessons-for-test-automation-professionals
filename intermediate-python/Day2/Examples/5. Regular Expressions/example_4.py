import re
# Caret
pattern = '^The'
texts = ['The dogs were barking',\
    'There were no dogs in the house',\
        'Yet, she kept on moving forward.']
for text in texts:
    num_matches = len(re.findall(pattern, text))
    print(num_matches,':',text)
