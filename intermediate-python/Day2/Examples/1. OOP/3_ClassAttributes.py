class XClass:
    class_variable = None

    def instance_method(self):
        self.class_variable = 200

obj = XClass()
# class variable does not belong to an instance
# so cannot assign using an instance of the class
obj.class_variable = 100 
print(XClass.class_variable)
obj.instance_method()
# Instances can access but not assign
print(obj.class_variable) 
XClass.class_variable = 300
print(XClass.class_variable)
