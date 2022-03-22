import sqlite3

choice = input('Reservatsiooni olemasolu kontrollimiseks valige "K", uue lisamiseks "U" \nSiia: ')
ühendus = sqlite3.connect('spa_database.db')
con = ühendus.cursor()

def uus_reserv():
    Eesnimi = input('NIMI: ')
    Perekonnanimi = input('PEREKONNANIMI: ')
    Inimesed = input('MITU INIMEST: ')
    Kellaaeg = input('MIS KELL: ')
    con.execute("""INSERT INTO spa_reservatsioonid(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg) VALUES (?, ?, ?, ?)""", (Eesnimi, Perekonnanimi, Inimesed, Kellaaeg))
    ühendus.commit()
    ühendus.close()

def kontroll():
    print('Kontroll')

con.execute('''CREATE TABLE IF NOT EXISTS spa_reservatsioonid
(Eesnimi TEXT,
Perekonnanimi TEXT,
Inimesed INTEGER,
Kellaaeg INTEGER)
''')


if choice.lower() == 'k':
    kontroll()
elif choice.lower() == 'u':
    uus_reserv()
    print('Uus reservatsioon on sisestattud')
else:
    print('Päring ebaõnnestus')
    
    
 

