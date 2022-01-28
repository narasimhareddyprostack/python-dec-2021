from abc import *
class Test:
    x = 100    #static variable
    @abstractmethod
    def m1(self):
        pass

t = Test()
print(t.__dict__)
print(Test.__dict__)
