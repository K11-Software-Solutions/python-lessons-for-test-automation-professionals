import threading  
import datetime  
import time

class ThreadClass(threading.Thread):  
	def run(self):
		date=datetime.datetime.now()  
		print("%s, Hello World! at: %s\n" \
			%(self.name, date))

for i in range(2):  
	t=ThreadClass()  
	t.daemon=True  
	t.start()
time.sleep(5)  
print("")

