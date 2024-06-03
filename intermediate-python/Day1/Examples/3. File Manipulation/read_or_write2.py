myfile=open(r"./code/myfile11.txt", "w+")  
names=["Bob\n", "Ted\n", "Carol\n", "Alice\n"]  
myfile.writelines(names)
myfile.close()

myfile=open(r"./code/myfile11.txt", "r")  
names=list(myfile.readlines())
for name in names:  
	print(name)
myfile.close()
