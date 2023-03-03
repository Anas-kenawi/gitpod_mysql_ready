import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

for x in range(5):
    r = input("Vuoi inserire un nuovo animale? ")
    if r=="si":
                   sql = "INSERT INTO Mammiferi_2 (nome_proprio, Razza, Peso, Età ) VALUES (%s, %s, %s, %s)"
                   nome = input("dimmi il nome ")
                   razza = input("dimmi la razza ")
                   peso = input("dimmi quanto pesa(in chili), scrivendo solo il numero ")
                   età = input("dimmi quanti anni ha, scrivendo solo il numero ")
                   
                   val =  (nome, razza, peso, età)


