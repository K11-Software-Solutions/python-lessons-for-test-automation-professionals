import threading  
import datetime  
import time

class ThreadClass(threading.Thread):  
	def run(self):
		date=datetime.datetime.now()  
		print("%s, Hello World! at: %s\n" \
			%(self.name, date))
		time.sleep(5)

for i in range(2):  
	t=ThreadClass()  
	t.daemon=True  
	t.start()
	# t.join() # Uncomment to wait for thread to finish
print("")

