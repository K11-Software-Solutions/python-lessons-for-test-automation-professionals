status="executive"  
if(status.lower()=="exempt"):
	print("Paid Salary + Bonus")  
else:
	if(status.lower()=="hourly"):  
		print("Pay Hourly + overtime")
	else:
		if(status.lower()=="executive"):  
			print("Pay Salary + Bonus + Stock")


# Switching with if elseif

today="FRi"  
today=today.capitalize()  
print(today)
if today=="Sun":
	print("Start of the week")  
elif today=="Mon":
	print("Start of work week")  
elif today=="Tue":
	print("Another day")  
elif today=="Wed":
	print("Hump day")  
elif today=="Thu":
	print("Almost over")  
elif today=="Fri":
	print("Time for celebration")  
elif today=="Sat":
	print("All day / all fun")  
else:
	print("This is a weird day!")

