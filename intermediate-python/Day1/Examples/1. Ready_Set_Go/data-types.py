# Runtime type info
a = 5   
print(type(a))
print(isinstance(a,int))

# Operators
x,y = 5,10
print(f'{x} + {y} = ', x + y)
print(f'{x} - {y} = ', x - y)
print(f'{x} / {y} = ', x / y)
print(f'{x} * {y} = ', x * y)
print(f'{x} // {y} = ', x // y)
print(f'{x} % {y} = ', x % y)

import sys

# Number of significant digits in a float
print('Float SIG:',sys.float_info.dig)