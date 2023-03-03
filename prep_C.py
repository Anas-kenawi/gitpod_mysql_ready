import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi_2")

myResult = mycursor.fetchall()

for x in myResult:
    print(x)