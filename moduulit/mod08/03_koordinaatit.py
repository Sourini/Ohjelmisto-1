# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy.distance import geodesic
import config

ap1 = []

def executeSQLsearch(sql, params):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    return cursor.fetchall()

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user=config.ur,
         password=config.pw,
         autocommit=True
         )

for i in range(2):
    icao = input('enter the ICAO code of the airport you are looking for: ')
    sql = "select latitude_deg,longitude_deg from airport where ident =%s"
    icaoList = [icao]
    if not ap1:
        ap1 = executeSQLsearch(sql, icaoList)
    else:
        ap2 = executeSQLsearch(sql, icaoList)


print(geodesic(ap1, ap2).kilometers)