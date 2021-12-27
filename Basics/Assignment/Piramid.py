n = int(input("Enter Number of Rows:"))
for i in range(1,n+1):
    print("A" * (n-i),end="")
    print("* " * i)
