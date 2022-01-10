def outer():
    print("Outer ")
    def inner():
        print("Inner ")
        return "Hello, Good Morning"

    return inner

#x = outer()   # calling funciton
y = outer      # function ref /function alisasing(anothor name)
y()
#
# message = x()
# print(message)