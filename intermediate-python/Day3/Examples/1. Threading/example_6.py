import threading  
import time

num_cabs = 5
sema=threading.Semaphore(num_cabs) 

def cab_allocation_thread():
    name=threading.current_thread().name  
    while(True):
        print("%s Requesting car\n"%name)
        sema.acquire(True)
        print("%s Shift started\n"%name)
        # 8 hour shift
        time.sleep(8)
        print("%s Off work\n"%name)
        sema.release()

        time.sleep(2)

num_drivers = 3
for d in range(num_drivers):
    t = threading.Thread(target=cab_allocation_thread)  
    t.daemon = True
    t.start()  

