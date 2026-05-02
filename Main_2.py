def Multiplication(Value1, Value2):
    Mult = 0
    Mult = Value1 * Value2
    return Mult

def main():
    
    No1 = int(input("Enter First Number:"))
    No2 = int(input("Enter Second Number:"))
    Result = 0

    Result = Multiplication(No1, No2)
    print("Multiplication is :", Result)

# Starter

if __name__ == "__main__":
    main()