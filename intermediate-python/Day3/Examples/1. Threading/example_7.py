import threading  
import time
theevent=threading.Event()  
def thethread():
    while(True):
        print("Thread running\n")
        if(not theevent.is_set()):
            print("Thread about to block\n")  
        theevent.wait()
        time.sleep(2)
        
t = threading.Thread(target=thethread)  
t.start()
time.sleep(5)  
print("Set Event")  
theevent.set()  
time.sleep(10)  
print("Reset Event")  
theevent.clear()  
time.sleep(5)
