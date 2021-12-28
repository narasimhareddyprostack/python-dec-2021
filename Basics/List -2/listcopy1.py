#copy function

a = [1,2,3]
b = a.copy()
c = a[:]
b[1] = 100
c[1] = 400
print(a)
print(b)
print(c)
