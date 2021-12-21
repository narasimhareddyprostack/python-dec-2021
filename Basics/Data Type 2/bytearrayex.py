size = [38,40,42,44]
ba = bytearray(size)
b =bytes(size)

print(type(size))  # list
print(type(ba))    # bytearray
print(type(b))     # bytes

ba[0]=39   # assignment is possible
#b[0]=39   # element modify/assignment not possbile
print(ba[0])

#what is bytearray?