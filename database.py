import mysql.connector as myc
mydb = myc.connect(
    host='localhost',
    user='root',
    password='whitny5963'
)

mycursor = mydb.cursor()
mycursor.execute("show tables;")
for x in mycursor:
    print(x)