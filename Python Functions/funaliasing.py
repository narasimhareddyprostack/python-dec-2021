def add():
    print("addition")

x = add
print(id(x))
print(id(add))

x()
add()

del add
x()
add()

