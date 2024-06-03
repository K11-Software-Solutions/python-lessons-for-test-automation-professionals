from collections import namedtuple

Constants = namedtuple('Constants', ['pi', 'e'])
constants = Constants(3.14, 2.718)
print(constants.pi)
constants.pi = 3
