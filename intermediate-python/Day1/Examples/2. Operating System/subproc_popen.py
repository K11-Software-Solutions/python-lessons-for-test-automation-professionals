import subprocess
p = subprocess.Popen(r"py names.py",  
shell=True, stdout=subprocess.PIPE,  
stderr=subprocess.STDOUT)

for line in p.stdout.readlines():  
	print(line)

retval = p.wait()
