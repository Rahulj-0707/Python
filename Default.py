def EmployeeInfo(Name = "Gotya", Age = 21, Salary = 10000, City = "Mumbai"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():

    # Keyword arguments
    
    #EmployeeInfo(Age = 26, Name = "Rahul", City = "Pune", Salary = 50000.50) # Correct
    EmployeeInfo()
    
if __name__ == "__main__":
    main()