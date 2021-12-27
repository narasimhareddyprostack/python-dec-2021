#creation of List Objects
a = []
print(a)
print(type(a))

#If you know elements
a = [10,20,30,40]
print(a)

#with list()  - inbuilt function

size = list(range(38,47,2))
print(size)
print(type(size))


#split() function
message = "Welcome to Pro Stack Academy"
l = message.split()
print(l)
print(type(l))

#input function with eval()
newSize = eval(input("Enter Size with list formmat:"))
print(newSize)
print(type(newSize))