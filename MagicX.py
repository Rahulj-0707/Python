#Dunder Method / Magic Method / Special Method

class Demo:
    def __init__(self, A):
        self.No = A

    def __add__(self,Other):
        return self.No + Other.No
    
    def __sub__(self,Other):
        return self.No - Other.No
    
    def __mul__(self,Other):
        return self.No * Other.No
    
    def __truediv__(self,Other):
        return self.No / Other.No
    

    
obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2)   #__add__(obj1, obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)  