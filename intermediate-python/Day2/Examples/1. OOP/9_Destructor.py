class P:

    def __init__(self,x):
        self.__x = x
        self.y = x

    def __del__(self):
        print("destructor called")
        
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    @x.deleter
    def x(self):
        print("deleter called on property")
        del self.__x


obj=P(10)
del obj.x
print(obj)
