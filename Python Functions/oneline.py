def fun1(a):
    return a+1

lambda  a:a+1

#map(lambda  a:a+1, [1,2,3,4])
l2=list(map(fun1, [1,2,3,4]))
print(l2)

print(list(map(lambda a:a+1, [1,2,3,4])))
