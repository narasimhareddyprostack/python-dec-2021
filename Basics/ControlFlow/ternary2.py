a = int(input("Please Enter First Number:"))
b = int(input("Please Enter Second Number:"))
c = int(input("Please Enter First Number:"))
min = a if a<b and a<c else b if b<c else c 
print(min)