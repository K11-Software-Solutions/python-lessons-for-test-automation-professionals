import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="[%(levelname)s] (%(threadName)s) : %(message)s")

def thethread(arg):
    print('Worker %d\n'%arg)
    logging.debug('Worker %d\n'%arg)
    
threads = []

for i in range(5):
    t = threading.Thread(target=thethread,args=(i,))
    t.start()

time.sleep(5)