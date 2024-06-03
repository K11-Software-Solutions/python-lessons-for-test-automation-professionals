import os

filename="test.txt"  
extfilename=r".\test.txt"  
dirname= r".\\"  
dirname2=r".\code"  
dirname3=r".\code\one\two\three"
print("Listdir  = ", os.listdir(dirname))
print("Join  = ", os.path.join(dirname, filename))
print("Stat  = ", os.stat(dirname))
print("Stat= ", os.stat(extfilename))
#print("Mkdir  = ", os.mkdir(dirname2))
print("Makedirs = ", os.makedirs(dirname3))





