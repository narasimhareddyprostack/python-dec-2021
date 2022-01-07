price = 500      #global variable
def add():
    price = 100  #local variable
    discount = 5
    print(price) #100
    print(discount)

def display():
    print(price) #500
    print(discount)

add()
display()