class User:
    deposit_Amount = 500
    def __init__(self,id,name,org_Name):
        self.id = id
        self.name=name
        self.org_Name = org_Name
        print("executing automatically")
    def get_Details(self):
        print(self.name)
        print("User Id: {}\n Name:{} \n Org Name: {}".format(self.id, self.name,self.org_Name))

u1 = User(101,'Narasimha', 'Pro Stack')
u1.get_Details()
print(u1.__dict__)