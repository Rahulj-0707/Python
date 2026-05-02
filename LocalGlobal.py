No = 11   # Global Veriable 

def Fun():
    No = 21  # Local Veriable
    print("Value of No from Fun is :", No)  #21

print("Value of No is ", No) #11
Fun()