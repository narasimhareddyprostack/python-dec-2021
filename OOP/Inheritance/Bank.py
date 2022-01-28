class Bank:
    def open_Account(self):
        print("Account Open Successfully!")
    def close_Account(self):
        print("Account Closed")

class Savings_Account(Bank):
    def deposit_Amount(self):
        print("Amouont is Deposited")

c1 = Savings_Account()
c1.open_Account()
c1.deposit_Amount()
c1.close_Account()