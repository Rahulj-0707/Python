# Procedural Approach
def ChkEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False
    
def main():
    Value = 0
    Ret = False

    print("Enter a number:")
    Value = int(input())

    Ret = ChkEven(Value)

    print(Ret)

if __name__ == "__main__":
    main()