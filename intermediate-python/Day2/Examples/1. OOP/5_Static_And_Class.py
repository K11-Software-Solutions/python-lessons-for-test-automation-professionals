class XClass:
    count=0

    @classmethod  
    def Func1(cls):
        cls.count = cls.count+1

    @staticmethod  
    def Func2(cls):
        cls.count = cls.count+1	# not work  
        pass

obj = XClass()  
XClass.Func1()  
XClass.Func2()
