def sum(*n):
    total=0
    for value in n:
        total = total+value
        
    print(total)

	
sum()
sum(10)
sum(10,20)
sum(100,200,400,500,5000)


'''
()
(10,)
(10, 20)
(10, 20, 30)
(10, 20, 30, 40)
'''