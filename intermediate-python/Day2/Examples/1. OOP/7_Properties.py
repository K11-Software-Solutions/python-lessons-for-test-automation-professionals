

class Person:
	def init (self):  
		self.__ageunknown=1

	def SetAge(self, _age):
		if(_age < 0 or _age > 120):  
			return False
		self.__ageunknown=_age  
		return True

	def GetAge(self):
		return self.__ageunknown

bob=Person()
if(bob.SetAge(54)):  
	print(bob.GetAge())
