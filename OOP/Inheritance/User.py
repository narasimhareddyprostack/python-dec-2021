class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
class Employee(User):
    def __init__(self, eno,ename, esal, eage):
        super().__init__(ename,eage)
        self.eno = eno
        self.esal = esal
    def getSal(self):
        print(self.esal)

e = Employee(101,"Rahul Gandhi", 45000, 50)
print(e.__dict__)
e.getName()
e.getSal()