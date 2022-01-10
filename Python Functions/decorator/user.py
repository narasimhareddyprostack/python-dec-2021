def user_Upper(func):
        def inner():
            message = func()
            return message.upper()

        return inner


def print_User():
    return "hi, rahul gandhi"

d = user_Upper(print_User)
print(d())