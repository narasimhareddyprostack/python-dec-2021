class Employee:
    org_Name = "TCS"
    def __init__(self,name):
        self.name = name

e1 = Employee('Rahul Gandhi')
e2 = Employee('Sonia')

print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)