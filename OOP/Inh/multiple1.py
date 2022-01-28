class Father:
    def m1(self):
        print("Father - m1() method")
class Mother:
    def m1(self):
        print("Mother- m1() method")

class Child(Mother,Father):
    def m3(self):
        print("Child - m3() method")

c = Child()
c.m1()