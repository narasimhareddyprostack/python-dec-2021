l = [10,20,30]
def addone(x):
    return x+2
#create a new list obj based on map()
l1 = list(map(addone,l))
print(l1)

l2 = list(map(lambda x:x+2, l))
print(l2)