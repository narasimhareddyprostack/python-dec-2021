a = [1,2,3]
b = a
b[1] = 200
print(a)
print(b)
print(id(a))
print(id(b))