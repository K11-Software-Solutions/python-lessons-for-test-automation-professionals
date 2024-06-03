class Parent:
    def __init__(self):
        print("Parent c'tor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child c'tor")

obj=Child()
