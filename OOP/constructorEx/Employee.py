class Employee:
    def __init__(self,a,b,c):
        self.emp_Id= a
        self.emp_Name=b
        self.emp_Sal = c

    def employee_Details(self):
        print("Displaying Employee Detaisl")

e1 = Employee(101,"Sujatha",45000)
e1.employee_Details()