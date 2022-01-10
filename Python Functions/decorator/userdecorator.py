def user_Upper(func):
    def inner():
        message = func()
        return message.upper()

    return inner

@user_Upper
def print_User():
    return "hi, rahul gandhi"

print(print_User())

