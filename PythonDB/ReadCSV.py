import csv
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #print(type(spamreader))
    list1 =[]
    for row in spamreader:
        #print(tuple(row))
        list1.append(tuple(row))


print(list1)