from collections import namedtuple

class XClass:
    constants = namedtuple('Constants', ['pi', \
                'e'])(3.14, 2.718)
        
print(XClass.constants.pi)
# XClass.constants.pi = 3
