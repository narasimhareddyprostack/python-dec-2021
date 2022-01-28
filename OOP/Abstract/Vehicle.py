from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofWheels(self):
        pass

class Bus(Vehicle):
    def noofWheels(self):
        return 10

class Auto(Vehicle):
    def noofWheels(self):
        return 3

b = Bus()
print(b.noofWheels())
a = Auto()
print(a.noofWheels())