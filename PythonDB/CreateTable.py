#help("modules")
import mysql.connector

try:
    dbobj = mysql.connector.connect(host='localhost',user="root",password="root", database="test")
    if dbobj:
        print("Connection Successfull")
    dbcursor =dbobj.cursor()
    dbcursor.execute('create table user1(uid int, uname varchar(30),  uemail varchar(30), gender varchar(20),dummy varchar(5))')
    print("Table Created")

except mysql.connector.DatabaseError as e:
    print(e)