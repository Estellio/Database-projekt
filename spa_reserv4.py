import sqlite3

choice = input('Reservatsiooni olemasolu kontrollimiseks sisestagage "K", uue lisamiseks "U" \nsiia: ')
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
    kellaaeg = input('Kellaaeg (00:00): ')
    con.execute('INSERT INTO spa_reservatsioonid(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg) VALUES (?, ?, ?, ?)', (eesnimi.title(), perekonnanimi.title(), inimesed, kellaaeg))
    ühendus.commit()
    ühendus.close()

def kontroll(eesnimi1, p_nimi1):
    kontroll = con.execute(('SELECT * FROM spa_reservatsioonid WHERE Eesnimi = ? AND Perekonnanimi = ?'), (eesnimi1.title(), p_nimi1.title()))
    check = kontroll.fetchall()
    if not check:
        ask = input('Reserveeringut ei ole andmebaasis. Kas soovite selle lisada? (Jah/Ei) ')
        if ask.lower() == 'jah':
            lisa_reserv(eesnimi1, p_nimi1)
            print('Uus reservatsioon on lisatud')
            print('Täname külastamast!')
        else:
            print('Täname külastamast!')
    else:
        print('Reserveering on olemas.')
        print('Täname külastamast!')
        
def lisa_reserv(eesnimi, p_nimi):
    inimesed = input('Inimeste arv: ')
    kellaaeg = input('Kellaaeg (00:00): ')
    con.execute('INSERT INTO spa_reservatsioonid(Eesnimi, Perekonnanimi, Inimesed, Kellaaeg) VALUES (?, ?, ?, ?)', (eesnimi, p_nimi, inimesed, kellaaeg))
    ühendus.commit()
    ühendus.close()

if choice.lower() == 'k':
    eesnimi = input('Nimi: ')
    p_nimi = input('Perekonnanimi: ')
    kontroll(eesnimi, p_nimi)
elif choice.lower() == 'u':
    uus_reserv()
    print('Uus reservatsioon on lisatud')
    print('Täname külastamast!')
else:
    print('Päring ebaõnnestus')
    print('Täname külastamast!')