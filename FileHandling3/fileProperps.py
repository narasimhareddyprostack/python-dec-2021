f = open('one.txt','r')

#  f - file ojbect 
# File Object Properties
print(f.name)
print(f.mode)
print(f.readable())
print("Writable or Not:",f.writable())
print(f.closed)
f.close()

