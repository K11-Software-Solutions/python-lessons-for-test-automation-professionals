
st = "hello привет नमस्ते" 
test=bytearray(st, "utf-8")
print(list(test))

_bytes=bytes(st, "utf-8")

# Fails because st is UTF-8
asciitest=bytes(st, "ascii")

print(_bytes)
for x in _bytes:
    print(x)

print(asciitest)
for x in _bytes:
  print(x)
