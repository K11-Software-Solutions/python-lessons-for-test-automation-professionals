# Reusable fried decorator
def fried(func):
    def new_function(*args, **kwargs): 
        func(*args, **kwargs)  
        number=args[0]
        quantity="is/are"  
        if(isinstance(number,int)):
            if not number:
                raise Exception("Number equal 0")  
            number = abs(number)
            quantity="are" if number > 1 and func.__name__ != 'beef' else "is"  
            print(", which %s fried."%quantity)
    return new_function

@fried
def egg(number):  
	if(isinstance(number, int)):
		print("You have %d egg(s)"%abs(number), end="")  
	else:
		print("You have eggs", end="")

@fried
def beef(number,type):  
	if(isinstance(number, int)):
		print(f"You have {abs(number)} {type} beef", end="")  
	else:
		print("You have {type} beef", end="")
        
egg(12)
beef(3,'Stur Fry')
