class Demo:
    No = 10

    def __init__(self,A, B):
        self.Value1 = A
        self.Value2 = B

    def Fun(self):
        print("Inside Instance Method Fun : ",self.Value1, self.Value2)
    
    @classmethod         #decorator
    def Sun(cls):
        print("Inside Class Method Sun : ", cls.No)

    @staticmethod
    def Gun():
        print("Inside Static Method Gun : ", Demo.No)

Demo.Sun()
print("Class Verialbe No :", Demo.No)

obj = Demo(11, 21)

obj.Fun()
print("Instance Variable :", obj.Value1, obj.Value2)

obj.Sun()

Demo.Gun()