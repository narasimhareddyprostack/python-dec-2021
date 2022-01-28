class Test:
    @staticmethod
    def add(x,y):
        print(x+y)

    @staticmethod
    def multi(x,y):
        print(x*y)

    def getData(self):
        pass

    @classmethod
    def m1(cls):
        pass

Test.add(5,6)
Test.multi(10,20)