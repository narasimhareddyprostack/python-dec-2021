import mysql.connector
import csv




try:
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # print(type(spamreader))
        list1 = []
        for row in spamreader:
            # print(tuple(row))
            list1.append(tuple(row))

    dbobject = mysql.connector.connect(host='localhost', user="root", password="root", database="test")
    dbcursor = dbobject.cursor()
    # read csv for data from file
    # read data form excel
    sql = 'insert into user1(uid, uname,uemail, gender,dummy) value(%s,%s,%s,%s,%s)'



    #list1 = [(106,'Rushika',75000),(107,'Rushika1',75000),(108,'Rushika2',75000),(109,'Rushika3',75000)]
    print(list1)
    dbcursor.executemany(sql,list1);
    dbobject.commit()
    print('Inserted Successfully ')

except mysql.connector.DatabaseError as e:
    print(e)