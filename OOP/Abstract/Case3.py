from abc import *

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

t1 = Test()


#Can't instantiate abstract class Test with abstract methods m1
