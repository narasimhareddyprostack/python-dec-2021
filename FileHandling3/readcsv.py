import csv

f = open( 'test.csv','r')
#csv reader object
robj = csv.reader(f)

for line in robj:
    for word in line:
        print(word,"\t", end="")
    print()