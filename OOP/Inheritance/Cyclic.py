class Bank:
    count = 0
    def __init__(self):
        Bank.count = self.count +1

c1 = Bank()
c2 = Bank()
c = Bank()
print(Bank.count)
