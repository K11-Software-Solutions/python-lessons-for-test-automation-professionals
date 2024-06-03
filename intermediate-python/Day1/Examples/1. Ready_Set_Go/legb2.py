glob = 1

def foo():
    loc = 5
    print('loc in foo():', \
      'loc' in locals())
    
print('loc in foo():', \
      'loc' in locals())

print('foo in global:', \
      'foo' in globals())

foo()

print('loc in global:', \
      'loc' in globals())

print('glob in global:', \
      'foo' in globals())
