class Parent:
    def m1(self):
        print("Parent Class m1 () method")
class Boy(Parent):
    pass
class Girl(Parent):
    pass

b = Boy()
b.m1()
g = Girl()
g.m1()