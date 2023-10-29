import mysql.connector


def suoritaSQLhaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

icao = input('anna haluamasi kentän ICAO-koodi: ')
sql = "select name, municipality from airport where ident ='" + icao + "'";
tulos = suoritaSQLhaku(sql)
for rivi in tulos:
    print(rivi)
