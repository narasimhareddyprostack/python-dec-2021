a=10
def greet():
    global b
    b=20
    a=1000
    print(a)

greet()

print(a)
print(b)