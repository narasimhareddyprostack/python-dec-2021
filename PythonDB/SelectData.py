import mysql.connector

try:
    dbobj = mysql.connector.connect(host='localhost', user="root",password="root", database="test")
    dbcursor = dbobj.cursor()
    dbcursor.execute('select * from employee')
    data = dbcursor.fetchall()
    #print(type(data))
    #print(data)
    for row in data:
        #print(type(row))
        print("Employee Id:",row[0], "Employee Name:", row[1], "Employee Salary:", row[2])

except mysql.connector.DatabaseError as e:
    print(e)