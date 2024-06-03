import threading
import time

def thethread():
    print('Worker\n')
    return

for i in range(5):
    t = threading.Thread(target=thethread)
    t.start()

time.sleep(10)