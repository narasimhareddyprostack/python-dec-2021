class Bank:
    def __init__(self,id,name):
        self.id = id
        self.name= name
    def getName(self):
       return self.name
    def setName(self):
        self.name = "Rahul"

c1 = Bank(101, "Rahul Gandhi")
c1.setName()
print(c1.getName())
