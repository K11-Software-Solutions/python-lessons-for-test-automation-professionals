import os


files=len(os.listdir(r"./"))

print("Files = ", files)

total=sum([os.path.getsize(f) \
           for f in os.listdir(r"./") \
           if os.path.isfile(f)])

print("Bytes = ",total)

