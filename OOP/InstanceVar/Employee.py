class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def setSal(self):
        self.salary  = 45000
e1 = Employee(101,'Rahul Gandhi')
e2 = Employee(102,'Sonia Gandhi')
e1.setSal()
e2.setSal()
e1.loc = "New Delhi"
print(e1.__dict__)
print(e2.__dict__)