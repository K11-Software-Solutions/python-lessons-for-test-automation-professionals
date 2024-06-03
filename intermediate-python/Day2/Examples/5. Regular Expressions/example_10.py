import re
# alternation
pattern = 'hello|ola'

# match any string that contains hello or olla
words = ['"Hello!", yelled the squire.', \
    'King Olaf of Norway','Helios the space company']
for w in words:
    print(w,re.findall(pattern,w.lower()),sep=':\t\t')