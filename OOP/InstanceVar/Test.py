class Test:
    def __init__(self):
        self.a = 100
        self.b= 200
        self.c = 300

t1 = Test()
t2 = Test()
del t1.b
del t2.a
t1.c = 3000
print(t1.__dict__)
print(t2.__dict__)