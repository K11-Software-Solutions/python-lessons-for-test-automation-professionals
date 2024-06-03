class RequiredField:

    def __set_name__(self, owner, name):
        print(f'__set_name__ was called with owner:{owner} and name:{name}')
        self.property_name = name

    def __get__(self,instance,owner):
        print(f'__get__ was called with instance:{instance} and owner:{owner}')
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self,instance,value):
        print(f'__set__ was called with instance:{instance} and value:{value}')

        if not isinstance(value,str):
            raise ValueError(f"{self.property_name} must be a string")
        
        if len(value) == 0:
            raise ValueError(f"{self.property_name} cannot be empty")

        instance.__dict__[self.property_name] = value

class Person:
   
    firstname = RequiredField()
    lastname = RequiredField()


obj = Person()
obj.firstname = 'James'
obj.lastname = 'Doro'

print(obj.firstname)