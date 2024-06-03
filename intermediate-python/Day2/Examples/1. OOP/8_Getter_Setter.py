class Person:
	def init (self):  
		self.__ageunknown=1

    # Getter
	@property
	def age(self):
		return self.__ageunknown

	@age.setter
	def age(self, _age):
		if(_age < 0 or _age > 120):
			raise Exception("Invalid Age")  
		self.__ageunknown=_age

	@age.deleter  
	def age(self):
		raise TypeError("Can't Delete")


bob=Person()  
try:
    bob.age=54  
    print(bob.age)  
    del bob.age
except Exception as e:  
	print(e)
