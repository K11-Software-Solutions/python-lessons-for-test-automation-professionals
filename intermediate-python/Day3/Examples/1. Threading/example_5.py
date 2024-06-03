import threading  
import time

thelock=threading.Lock()  

def thethread():
	name=threading.current_thread().name  
	for i in range(3):
		#protect resource  
		thelock.acquire()
		print("%s enters gate"%name)  
		time.sleep(1)
		print("%s leaves gates"%name)  
		thelock.release()  

count=5  
while(count):
    print("%d starting"%count)
    t = threading.Thread(target=thethread,name=f'Thread-{count}')  
    t.daemon = True
    t.start() 
    count-=1

print("All threads finished")