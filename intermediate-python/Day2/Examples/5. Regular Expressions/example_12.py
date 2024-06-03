import re

txt = "The impact of COVID-19 on\
     supply chains was not good for business."
x = re.findall("supply", txt)
print(x)