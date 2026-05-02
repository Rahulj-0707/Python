class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

        print("object get created successfully:")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmatic(11,10)
obj2 = Arithmatic(21,20)

Ret = obj1.Addition()
print("Addition is : ", Ret)

Ret = obj2.Substraction()
print("Substraction is : ", Ret)
    
        