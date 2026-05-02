def EmployeeInfo(Name, Age, Salary, City = "Mumbai"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():

    # Keyword arguments
    
    #EmployeeInfo(Age = 26, Name = "Rahul", City = "Pune", Salary = 50000.50) # Correct
    EmployeeInfo("Rahul", 26, 50000.50)
    EmployeeInfo("Rahul", 26, 50000.50, "Pune")

    
if __name__ == "__main__":
    main()