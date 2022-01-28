class User:
    a = 100  #statc variale
    def __init__(self):
        self.b= 200    #instance variable
        print("User class/Super class - constructor")

    def m1(self):
        self.c = 300
        print("User class - m1 () method ")
    @classmethod
    def m2(cls):
        print("User class - m2() class method")
    @staticmethod
    def m3():
        print("User class  - m3 class method")

class Employee(User):
    def __init__(self):
        super().__init__()
        print(super().a)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()

e = Employee()