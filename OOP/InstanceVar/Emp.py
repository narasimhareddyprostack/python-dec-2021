class Emp:
    def __init__(self,id,name):
        self.id=id
        self.name = name

    def getDetails(self):
        print(self.id)
        print(self.name)
        del self.id

e1  = Emp(101,'Rahul')
e1.getDetails()
#print(e1.id)
print(e1.name)
print(e1.__dict__)
del e1.name
print(e1.__dict__)
