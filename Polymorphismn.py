class Parent:
    def __init__(self):
        print("Inside Parent constructor")

    def Fun(self):
        print("Inside Fun method of Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
        
    def Fun(self):
        super().Fun()
        print("Inside Fun Method of child")

cobj = Child()
cobj.Fun()