import pickle

myfile=open('./code/data.bin', 'wb+')
pickle.dump(9 ** 33, myfile)  
myfile.close()  
myfile=open('./code/data.bin', 'rb')
print(pickle.load(myfile))  
myfile.close()


