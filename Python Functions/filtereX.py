numbers =[1,2,3,4,5,6,7,8,9,10]

def odd_Number(num):
    if num % 2 != 0:
        return True
    else:
        return False



#print(list(map(odd_Number, number)))
#list(map())
result = list(map(odd_Number, numbers))
print(result)

[True, False, True, False, True, False, True, False, True, False]
print(list(filter(odd_Number, numbers)))
