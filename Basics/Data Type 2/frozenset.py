s = {10,20,10,True,False, 100,200, 'hello'}

fs = frozenset(s)
s.add('good monring')
print(type(s))
print(type(fs))
print(s)
#fs.add('good morning')

print(fs)