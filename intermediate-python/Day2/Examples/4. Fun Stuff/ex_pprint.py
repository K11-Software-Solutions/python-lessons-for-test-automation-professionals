from pprint import pprint


import pprint

data = list(range(0,20))
p = pprint.PrettyPrinter(indent=4,width=20)
p.pprint(data)