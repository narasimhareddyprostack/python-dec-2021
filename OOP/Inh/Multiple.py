class Parent1:
    def m1(self):
        print("Parent1 - m1() method")
class Parent2:
    def m2(self):
        print("Parent2- m2() method")

class Child(Parent1,Parent2):
    def m3(self):
        print("Child - m3() method")

c = Child()
c.m1()
c.m2()
c.m3()