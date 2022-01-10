from random import *

help(random)
'''
random()

'''
for i in range(5):
    print(random())

#random() - it generate random number between 0 to 1 (not inclusive)

for x in range(5):
    print(randint(1,1000))

employees = ['Rahul', 'priyanka', 'Sonia']
for y in range(10):
    print(choice(employees))