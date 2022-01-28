class Bank:
    min_Bal = 500
    @classmethod
    def set_Min_Bal(cls):
        cls.min_Bal = 5000

    def get_Min_Bal(self):
       return self.min_Bal

print(Bank.min_Bal)
c1 = Bank()
c1.set_Min_Bal()
print(Bank.min_Bal)
print("instance method callling",c1.get_Min_Bal())

