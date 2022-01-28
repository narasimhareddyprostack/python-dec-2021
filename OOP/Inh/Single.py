class Parent:
    def m1(self):
        print("Parent Classs -m1() method")
class Child(Parent):
    def m2(self):
        print("Child Class - m2() method")


c  = Child()
c.m1()
c.m2()
