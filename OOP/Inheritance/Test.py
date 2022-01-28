class Parent:
    def __init__(self):
        print("Parent class Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class Constructor")

Child()
