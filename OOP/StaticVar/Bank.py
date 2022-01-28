class Bank:
    min_Bal = 500   # static vairable
    def __init__(self,acc_Id, acc_Name):
        self.acc_Id = acc_Id    #instance
        self.acc_Name =acc_Name #instace
        Bank.branch_Name = "Marathahalli, Bangalore"

c1 = Bank(101,"Sujatha")
c2 = Bank(102,"Rushika")
c3 = Bank(103,"Ram")
print(c1.__dict__)
print(c2.__dict__)
print(c3.__dict__)
print(Bank.__dict__)