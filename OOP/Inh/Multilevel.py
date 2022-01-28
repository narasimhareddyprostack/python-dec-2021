class A:
    def m1(self):
        print("Class A- m1() Method")
class B(A):
    def m2(self):
        print("Class B- m2() Method")
class C(B):
    def m3(self):
        print("Class C- m3() Method")

c  = C()
c.m1()
c.m2()
c.m3()