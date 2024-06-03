import re

string = "The impact of COVID-19 on business."
pattern = '\s+'

result = re.split(pattern, string) 
print(result)