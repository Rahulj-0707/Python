def ChkEven(No):
    if (No % 2 == 0):
        print("It is Even Number")
    else:
        print("It is Odd Number")

def main():
    ChkEven(22) #positional
    ChkEven(No = 21) #Keyword

if __name__ == "__main__":
    main()
