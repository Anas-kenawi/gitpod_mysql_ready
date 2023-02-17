import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Animali")

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#  database="Animali"
#)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Mammiferi_2 (id INT AUTO_INCREMENT PRIMARY KEY, nome_proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Età INT)")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi_2 (nome_proprio, Razza, Peso, Età ) VALUES (%s, %s, %s, %s)"
val = [
  ()






