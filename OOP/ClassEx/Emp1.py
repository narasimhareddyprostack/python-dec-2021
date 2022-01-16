class Employee:
    a = 100
    def __init__(self):
        print("Executing automatically")

    def details(self):
        self.b = 200
        print("Displaying Employee Details")

e1 = Employee()
e1.details()
