class Test:
    amount = 500
    def __init__(self):
        Test.a = 100
        self.name="Rahul Gandhi"
    def m1(self):
        Test.b = 200
    @classmethod
    def m2(cls):
        cls.c = 300
        Test.d = 400
    @staticmethod
    def m3():
        Test.e = 500

t = Test()
t.m1()
t.m2()
t.m3()
print(t.__dict__)
print(Test.__dict__)