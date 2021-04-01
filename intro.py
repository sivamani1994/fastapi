import mysql.connector
## connecting to required database
connection=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='',
                                  database='prefix')

## getting the data from table
mycursor = connection.cursor()

mycursor.execute("SELECT * FROM  tblcountries")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)