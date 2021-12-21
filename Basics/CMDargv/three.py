from sys import argv
sum = 0
list = argv[1:]   #slicing
print(argv)
print(list)
for value in list:
    n = int(value)
    sum = sum + n 
    
print("Sum of CMD Arguments: ",  sum)
    