def update_Div(func):
    def inner(a,b):
        if b == 0 :
            #print("Cant devide")
            return "Cant Devide"
        else:
            return func(a,b)

    return inner

@update_Div
def division(a,b):
    return a/b

print(division(100,200))  # 0.5
print(division(10,0))     #error
print(division(10,2))