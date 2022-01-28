from abc import *

class Test(ABC):
    @abstractmethod
    def m1(self):
        print("Hello")

t1 = Test()
t2= Test()

print(t1)
print(t2)