myfile=open(r"./code/myfile10.txt", "w+") #w+ creates a file if it does not exist  
myfile.write("Bob\n")  
myfile.write("Ted\n")  
myfile.write("Carol\n")  
myfile.write("Alice\n")
myfile.close()

myfile=open(r"./code/myfile10.txt", "r")  
names=list(myfile.readlines())
for name in names:  
	print(name)
myfile.close()
