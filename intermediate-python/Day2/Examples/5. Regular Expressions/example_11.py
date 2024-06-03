import re
# group
pattern = '(hello|ola), how'

# match any string that contains hello or olla
words = ['Hello, how are you today?',\
    'Hello is a word used for greeting']
for w in words:
    print(w,re.findall(pattern,w.lower()),sep=':\t\t')