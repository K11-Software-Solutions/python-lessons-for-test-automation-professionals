import time

def Func():
    time.sleep(2)

start=time.time()
Func()
end=time.time()
elapse=int(end-start)

print("Elapsed time", elapse)
