class MyClass:
    def method(self):
        self.__class__.test=15
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        cls.test+=1
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    def staticmethod2():
        return 'static method2 called'


obj=MyClass()
print(obj.method())
print(MyClass.method(obj))

print(obj.classmethod())
print(MyClass.classmethod())

print(MyClass.test)

print(MyClass.staticmethod())
print(MyClass.staticmethod2())



