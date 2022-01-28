class Savings_Account:
    min_Bal = 500
    def __init__(self):
        print(self.min_Bal)
        print(Savings_Account.min_Bal)
    @classmethod
    def m1(cls):
        print("using cls variable - inside classmethod", cls.min_Bal)
        print("using className - inside classmethod",Savings_Account.min_Bal)

s = Savings_Account()
#print(s.min_Bal)
s.m1()
print(Savings_Account.min_Bal)