# Generic class without implementation
class Employee:
    
    # Constructor
    def __init__(self,firstname,lastname):
        print("C'structor called")
        self.firstname = firstname
        self.lastname = lastname

    # Destructor
    def __del__(self):
        print("D'structor called")

emp = Employee('James','Smith')
print(f"Fullname: {emp.firstname} {emp.lastname}")
del emp