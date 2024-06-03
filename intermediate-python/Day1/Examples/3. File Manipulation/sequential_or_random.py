
myfile=open("./code/greeting.txt", "w")  
myfile.write("Hello")  
myfile.close()
myfile=open("./code/greeting.txt", "r") 
print(myfile.tell())  
myfile.seek(3)  
print(myfile.tell())  
data=myfile.read(2)  
print(data)  
myfile.close()




