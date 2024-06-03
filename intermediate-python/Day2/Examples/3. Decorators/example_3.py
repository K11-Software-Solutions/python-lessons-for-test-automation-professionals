# Inefficient fried eggs code
def egg(number):
    print("You have %d egg(s)"%number, end="")

def fried(number): 
    if not number:
        raise Exception("Number equal 0")
    abs(number)
    egg(number)
    quantity="are" if number > 1 else "is"
    print(", which %s fried."%quantity)

fried(2)
