import  sqlite3
conn  =  sqlite3.connect ('spa_reserveering.db')
cursor  = conn.cursor()

nimi = input('NIMI: ')
perekonnanimi = input('PEREKONNANIMI: ')
inimesed = input('MITU INIMEST: ')

cursor.execute("""INSERT INTO spa_reserv(nimi, perekonnanimi, inimesed) VALUES (?,?,?)""", (nimi, perekonnanimi, inimesed))
conn.commit()
print ( 'Data entered successfully.' )
conn.close()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")