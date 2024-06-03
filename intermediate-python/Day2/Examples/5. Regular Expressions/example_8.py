# ? matches zero or one occurrences of the pattern
import re

pattern = "wi?n"
values = ['wn','wnn','win','wiiin'\
'wayne','winning','won']

for v in values:
    num_matches = len(re.findall(pattern, v))
    print(num_matches,':',v)

