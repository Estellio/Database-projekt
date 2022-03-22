import sqlite3

choice = input('Reservatsiooni olemasolu kontrollimiseks valige "K", uue lisamiseks "U" \n')
ühendus = sqlite3.connect('spa_database')
con = ühendus.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS spa_reservatsioonid
(Eesnimi TEXT,
Perekonnanimi TEXT,
Inimesed INTEGER,
Kellaaeg INTEGER)
''')

with open('spa_reservatsioonid.txt', 'r', encoding = 'utf-8') as fail:
    for rida in fail:
        elemendid = rida.strip('\n').split(';')
        con.execute('''INSERT INTO spa_reservatsioonid
(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg)
VALUES
(?, ?, ?, ?)''', (elemendid[0], elemendid[1], elemendid[2], elemendid[3]))
        ühendus.commit()

if choice.lower() == 'k':
    print('Kontroll')
elif choice.lower() == 'u':
    print('Uus reservatsioon')
else:
    print('Päring ebaõnnestus')