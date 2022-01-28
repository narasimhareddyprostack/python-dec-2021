class Savings_Account:
    min_Bal = 500
    def __init__(self):
        Savings_Account.min_Bal = 800
    @classmethod
    def m1(cls):
     cls.min_Bal = 700

s = Savings_Account()
print(Savings_Account.min_Bal)
s.m1()
print(Savings_Account.min_Bal)