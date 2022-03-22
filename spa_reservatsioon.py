import sqlite3

choice = input('Reservatsiooni olemasolu kontrollimiseks sisestagage "K", uue lisamiseks "U" \n')
fail = open('spa_reservatsioonid.txt', 'r', encoding = 'utf-8')
ühendus = sqlite3.connect('spa_database.db')
con = ühendus.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS spa_reservatsioonid
(Eesnimi TEXT,
Perekonnanimi TEXT,
Inimesed INTEGER,
Kellaaeg INTEGER)
''')

for rida in fail:
    elemendid = rida.strip('\n').split(';')
    kontroll = con.execute(('SELECT * FROM spa_reservatsioonid WHERE Eesnimi = ? AND Perekonnanimi = ?'),(elemendid[0], elemendid[1]))
    check = kontroll.fetchall()
    if not check:
        con.execute('''INSERT INTO spa_reservatsioonid
(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg)
VALUES
(?, ?, ?, ?)''', (elemendid))
        ühendus.commit()
    else:
        continue
fail.close()

def uus_reserv():
    eesnimi = input('Nimi: ')
    perekonnanimi = input('Perekonnanimi: ')
    inimesed = input('Inimeste arv: ')
    kellaaeg = input('Kellaaeg: ')
    con.execute('INSERT INTO spa_reservatsioonid(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg) VALUES (?, ?, ?, ?)', (eesnimi, perekonnanimi, inimesed, kellaaeg))
    ühendus.commit()
    ühendus.close()

def kontroll():
    eesnimi = input('Nimi: ')
    p_nimi = input('Perekonnanimi: ')
    # perekonnanime ees on tühik
    kontroll = con.execute(('SELECT * FROM spa_reservatsioonid WHERE Eesnimi = ? AND Perekonnanimi = ?'), (eesnimi, p_nimi))
    check = kontroll.fetchall()
    if not check:
        ask = input('Reserveeringut ei ole andmebaasis. Kas soovite selle lisada? (Jah/Ei) ')
        if ask.lower() == 'jah':
            uus_reserv()
            ühendus.commit()
    else:
        print('Reserveering on olemas.')

if choice.lower() == 'k':
    kontroll()
elif choice.lower() == 'u':
    uus_reserv()
    print('Uus reservatsioon on lisatud')
else:
    print('Päring ebaõnnestus')