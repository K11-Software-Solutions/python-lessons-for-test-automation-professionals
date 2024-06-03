import sys

class XClass:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0

obj = XClass()
a = 12

print(sys.getsizeof(obj))
print(sys.getsizeof(a))