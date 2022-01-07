def outer():
    print("Outer ")
    def inner():
        print("Inner ")
        return "Hello, Good Morning"

    return inner

x = outer()

message = x()
print(message)