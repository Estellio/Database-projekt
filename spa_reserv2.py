import sqlite3

choice = input('Reservatsiooni olemasolu kontrollimiseks valige "K", uue lisamiseks "U" \n')
ühendus = sqlite3.connect('spa_database.db')
con = ühendus.cursor()




con.execute('''CREATE TABLE IF NOT EXISTS spa_reservatsioonid
(Eesnimi TEXT,
Perekonnanimi TEXT,
Inimesed INTEGER,
Kellaaeg INTEGER)
''')


if choice.lower() == 'k':
    print('Kontroll')
elif choice.lower() == 'u':
    Eesnimi = input('NIMI: ')
    Perekonnanimi = input('PEREKONNANIMI: ')
    Inimesed = input('MITU INIMEST: ')
    Kellaaeg = input('MIS KELL: ')
    con.execute("""INSERT INTO spa_reservatsioonid(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg) VALUES (?, ?, ?, ?)""", (Eesnimi, Perekonnanimi, Inimesed, Kellaaeg))
    ühendus.commit()
    ühendus.close()
    print('Uus reservatsioon')
else:
    print('Päring ebaõnnestus')
    
    
 

