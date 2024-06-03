import os

file_obj = os.popen("echo Hello, World!")
print(type(file_obj))
print(file_obj.read())