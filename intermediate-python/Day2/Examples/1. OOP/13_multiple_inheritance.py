class One:
    def FuncA(self):
        print("One.FuncA()")

class Two:
    def FuncA(self):
        print("Two.FuncA()")

class Three:  
	pass

class Child(One, Two, Three):  
	pass

obj=Child()  
obj.FuncA()
