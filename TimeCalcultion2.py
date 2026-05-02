import time
def Factorial(No):

    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
   Value = int(input("Enter a Number : "))

   star_time = time.time()

   iRet = Factorial(Value)

   End_time = time.time()

   print("Factorial is",iRet)

   print("Total Execution time is",End_time - star_time)

if __name__ == "__main__":
    main()
