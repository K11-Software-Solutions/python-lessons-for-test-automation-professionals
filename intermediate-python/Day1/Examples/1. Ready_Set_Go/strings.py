helloinjapanese="こんにちは"
print(len("こんにちは"))
byteHello=bytes(helloinjapanese, "UTF-8")
print(len(byteHello))

print("Hello there.\nThis is a new line.")
# Raw string
print(r"Hello there.\nThis is a new line.")