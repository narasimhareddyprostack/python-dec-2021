#Calucate sum of first n number. ie 5 :  1+2+3+4+5 = 15
sum = 0

n = int(input("Enter Number:"))
i=1
while i<=n:
    sum = sum + i
    i = i+1

print("Sum of first n Numbers:", sum)
#print("Sum of first {} Number is: {}".format(n,sum))