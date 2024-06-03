from os import path
filename=r"names.py"  
dirname=r"c:\windows"
print("Exists =  ", path.exists(filename))
print("Dirname  =  ", path.dirname(filename))
print("Basename  =  ", path.basename(filename))
print("Split  =  ", path.split(filename))
print("GetSize  =  ", path.getsize(filename), " bytes")
print("GetSize  = ", path.getsize(dirname), " files")

