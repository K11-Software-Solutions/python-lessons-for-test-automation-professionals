import os

currentdir=".\\"  
os.chdir(currentdir)

for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))
    for dir in dirs:
        print(os.path.join(root, dir))
