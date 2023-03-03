import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi_2 WHERE Peso > 2")
myResult_2 = mycursor.fetchall()
for x in myResult_2:
    print(x)

