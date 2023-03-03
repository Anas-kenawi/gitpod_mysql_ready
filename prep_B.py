import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi_2 (nome_proprio, Razza, Peso, Età ) VALUES (%s, %s, %s, %s)"
val = [
  ("Alex", "leone", 190, 5),
  ("Marty", "zebra", 280, 17),
  ("Melman", "giraffa", 1600, 19),
  ("Gloria", "ippopotamo", 1500, 37),
  ("Skipper", "pinguino", 35, 17),
]

mycursor.executemany(sql, val)

mydb.commit()


