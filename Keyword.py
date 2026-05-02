def EmployeeInfo(Name, Age, Salary, City):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    # Positional
    #EmployeeInfo("Rahul", 25, 50000.50, "Pune") # Correct
    #EmployeeInfo(25, "Rahul", "Pune", 50000.50) # Wrong

    # Keyword
    
    EmployeeInfo(Age = 26, Name = "Rahul", City = "Pune", Salary = 50000.50) # Correct
    
if __name__ == "__main__":
    main()